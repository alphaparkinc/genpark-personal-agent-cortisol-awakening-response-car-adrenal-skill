# -*- coding: utf-8 -*-
"""MCP Server for Cortisol Awakening Response (CAR) & Adrenal Rhythm Skill."""
import sys
import json
import logging
from typing import Dict, Any

from .core import CortisolAwakeningResponseAdrenalCopilot

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

TOOLS_SCHEMA = [
    {
        "name": "audit_cortisol_awakening_curve",
        "description": "Evaluate 4-point diurnal salivary cortisol levels (Wake, Wake+30m, Afternoon, Night) to identify HPA axis dysregulation or flattened curve burnout.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "wake_cortisol_nmol_l": {
                    "type": "number"
                },
                "wake_plus_30m_cortisol_nmol_l": {
                    "type": "number"
                },
                "afternoon_cortisol_nmol_l": {
                    "type": "number"
                },
                "night_cortisol_nmol_l": {
                    "type": "number"
                }
            },
            "required": [
                "wake_cortisol_nmol_l",
                "wake_plus_30m_cortisol_nmol_l",
                "afternoon_cortisol_nmol_l",
                "night_cortisol_nmol_l"
            ]
        }
    },
    {
        "name": "prescribe_circadian_light_pacing",
        "description": "Calculate required morning lux exposure and evening melanopic light restrictions to re-anchor central suprachiasmatic nucleus (SCN) circadian phase.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "car_curve_status": {
                    "type": "string",
                    "enum": [
                        "FLATTENED_BURNOUT",
                        "BLUNTED_RESPONSE",
                        "NORMAL_HEALTHY",
                        "HYPER_REACTIVE_ACUTE_STRESS"
                    ]
                },
                "wake_time_hh_mm": {
                    "type": "string"
                }
            },
            "required": [
                "car_curve_status",
                "wake_time_hh_mm"
            ]
        }
    }
]

def handle_rpc(line: str) -> str:
    try:
        req = json.loads(line)
        method = req.get("method")
        msg_id = req.get("id")

        if method == "initialize":
            res = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-cortisol-awakening-response-car-adrenal-skill", "version": "1.0.0"}
            }
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": res})

        elif method == "tools/list":
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS_SCHEMA}})

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})

            target_func = getattr(CortisolAwakeningResponseAdrenalCopilot, tool_name, None)
            if not target_func:
                return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {tool_name}"}})

            result = target_func(**args)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result, indent=2)}]
                }
            })

        else:
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {method}"}})

    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": req.get("id") if "req" in locals() else None, "error": {"code": -32000, "message": str(e)}})

def run_test():
    print("[TEST] Running internal RPC self-test for genpark-personal-agent-cortisol-awakening-response-car-adrenal-skill...")
    init_req = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    init_res = json.loads(handle_rpc(init_req))
    assert init_res.get("result", {}).get("serverInfo", {}).get("name") == "genpark-personal-agent-cortisol-awakening-response-car-adrenal-skill"

    list_req = json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    list_res = json.loads(handle_rpc(list_req))
    assert len(list_res.get("result", {}).get("tools", [])) == 2
    print(f"[TEST] SUCCESS: {len(list_res['result']['tools'])} tools verified.")
    return True

if __name__ == "__main__":
    if "--test" in sys.argv:
        if run_test():
            sys.exit(0)
        sys.exit(1)

    for line in sys.stdin:
        if not line.strip():
            continue
        out = handle_rpc(line)
        sys.stdout.write(out + "\n")
        sys.stdout.flush()
