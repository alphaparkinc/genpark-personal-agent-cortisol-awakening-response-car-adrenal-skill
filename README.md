# Cortisol Awakening Response (CAR) & Adrenal Rhythm Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Salivary free cortisol awakening response (CAR) curve telemetry evaluation, HPA-axis adrenal burnout risk stratification, and morning photon flux lux/melanopic daylight pacing. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `audit_cortisol_awakening_curve`: Evaluate 4-point diurnal salivary cortisol levels (Wake, Wake+30m, Afternoon, Night) to identify HPA axis dysregulation or flattened curve burnout.
- `prescribe_circadian_light_pacing`: Calculate required morning lux exposure and evening melanopic light restrictions to re-anchor central suprachiasmatic nucleus (SCN) circadian phase.

## 🚀 Installation & Usage
Run directly with pure Python standard library:
```bash
python -m genpark_personal_agent_cortisol_awakening_response_car_adrenal_skill.server --test
```
