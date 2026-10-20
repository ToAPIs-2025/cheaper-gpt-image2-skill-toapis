# Cheaper GPT Image2 Skill · ToAPIs image CLI


<!-- TOAPIS-MODELS-20261020 -->
## Model support and prices · 2026-10-20

Added standalone API presets: 31 image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid calls while pricing is unavailable. Native provider/UI/import/render acceptance remains as documented in the original guide below.

| Image model / tested preset | Current preset quote / image | Historical example amount / image | Fee evidence |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | Billing log, phase unknown |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | Current-key quote unavailable | **$0.005272/image**<br><sub>Token-metered; current $/M unavailable. This sample is not a fixed image tariff.</sub> | Task receipt settled |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | Billing log, phase unknown |
| qwen-image-3.0<br><sub>1K</sub> | Current-key quote unavailable | **$0.021/image** | Billing log, phase unknown |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | Billing log, phase unknown |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | Billing log, phase unknown |

| Video model | Preset / input | Settled clip charge | File duration | Case USD/s, ascending |
|---|---|---:|---:|---|
| MiniMax-H3-Max-Turbo | 5s / 480P / text-to-video | $0.125/clip | 5.18s | **$0.024131/s**<br><sub>Pricing tariff: $0.025/s</sub> |
| seedance-2-mini | 4s / 480p / first-frame | $0.13338/clip | 4.04s | **$0.033015/s**<br><sub>Pricing tariff: $3.285714/M total tokens</sub> |
| seedance-2-fast | 4s / 480p / text-to-video | $0.214568/clip | 4.04s | **$0.053111/s**<br><sub>Pricing tariff: $5.285714/M total tokens</sub> |
| kling-v3 | 5s / 720p / std / text-to-video | $0.3/clip | 5.04s | **$0.059524/s**<br><sub>Pricing tariff: $0.06/s</sub> |
| MiniMax-H3 | 5s / 768p / text-to-video | $0.32/clip | 5.17s | **$0.061896/s**<br><sub>Pricing tariff: $0.064/s</sub> |
| seedance-2 | 4s / 480p / first-frame | $0.26676/clip | 4.04s | **$0.06603/s**<br><sub>Pricing tariff: $6.571429/M total tokens</sub> |
| kling-3.0-turbo | 4s / 720p / text-to-video | $0.32/clip | 4.04s | **$0.079208/s**<br><sub>Pricing tariff: $0.08/s</sub> |
| seedance-2-5 | 4s / 480p / text-to-video | $0.3883/clip | 4.04s | **$0.096114/s**<br><sub>Pricing tariff: $10/M total tokens</sub> |

Pricing checked 2026-10-20. Image examples are dated 2026-10-17; video examples 2026-10-20. Tables sort by example amount or case USD/s. Presets and input modes differ; this is not a matched-settings quality ranking. Unknown-phase image logs are not confirmed final net settlements. Current quotes and historical amounts are separate. Video charges are billing=settled; case USD/s divides charge by actual file duration, never processing time. Token tariffs appear in small text and do not imply a fixed per-second price.

gpt-image-2(VIP) starts at $0.0019/image; this low/1K preset is $0.0019/image. The standalone sampler has 31 historically successful image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid submission until an exact price is available.

[Local sampler](toapis-models/README.md) · [Full price table](PRICING.md) · [Original media and fee evidence](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/model-support-2026-10-20)

Original project examples, historical charges and integration instructions follow. Historical amounts are not rewritten as today’s quotes.

<!-- /TOAPIS-MODELS-20261020 -->

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## Tested model types, presets and costs

Updated October 16, 2026. These are tested historical presets/prices; this addition does not relabel the original batch below.

| Model (API ID) | Type | Tested preset | Unit quote | Confirmed unit charge | Count |
|---|---|---|---:|---:|---:|
| gpt-image-2(VIP) (`gpt-image-2-vip`) | Image | low / 1K / n=1 | $0.0019/image | $0.0019 | 3 |
| gpt-image-2 | Image | 1K / n=1 | $0.015/image | $0.015 | 1 |

Confirmed original image/video example subtotal: **$0.0207**.

Patched CLI image generation/edit path validated; agent-host execution and video are unvalidated.

gpt-image-2(VIP), **from $0.0019/image**; the tested low/1K preset here is **$0.0019/image**. Different models, qualities and resolutions do not imply equivalent results.
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

<!-- TOAPIS-IMAGE-SAMPLES-20261017 -->
## Same prompt: 8 image models and example costs

Tested **2026-10-17**: the same text-to-image prompt, one output per example, sorted by example amount from low to high. **gpt-image-2(VIP) starts at $0.0019/image; low/1K here is $0.0019/image.**

Each row identifies a task settlement receipt or an account billing log. Unknown-phase logs are not final net settlements; model/time-window candidates are not confirmed task matches. Catalog rates are historical quotes, not locked prices. gpt-image-2.5-flare-vip is token-metered: **$0.005272 is this image's settled charge**, not a fixed image rate. It is a different API ID from gpt-image-2.5-flare. Qwen has no returned key quote; only its example log amount is shown.

The prompt is shared, but quality defaults and output dimensions differ. Request presets and actual pixels are listed separately. Seedream Pro requested 1K with quality omitted (medium quoted), and returned 2048×2048. These are independent ToAPIs API asset tests; they do not extend any project's native-provider, UI, import or video validation, and are not added to the historical project subtotal below.

| Model / API ID | Request preset → actual pixels | Catalog rate (2026-10-17) | Example amount USD ↑ | Cost evidence | Real output |
|---|---|---:|---:|---|---|
| gpt-image-2(VIP)<br><code>gpt-image-2-vip</code> | 1K / low → 1024×1024 | $0.0019/image | **$0.0019** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png" width="112" alt="gpt-image-2(VIP) product image"></a> |
| gpt-image-2.5-flare-vip | 1024x1024 / low → 1024×1024 | Token-based; key quote unavailable | **$0.005272** | Task receipt: settled | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png" width="112" alt="gpt-image-2.5-flare-vip product image"></a> |
| nano_banana | 1K / default → 1024×1024 | $0.012/image | **$0.012** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png" width="112" alt="nano_banana product image"></a> |
| gemini-nano-banana-2.1 | 1K / default → 1024×1024 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg" width="112" alt="gemini-nano-banana-2.1 product image"></a> |
| gpt-image-2 | 1K / default → 1280×1280 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png" width="112" alt="gpt-image-2 product image"></a> |
| qwen-image-3.0 | 1K / default → 1024×1024 | Key quote unavailable | **$0.021** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png" width="112" alt="qwen-image-3.0 product image"></a> |
| gpt-image-2.5-flare | 1K / high → 1024×1024 | $0.0225/image | **$0.0225** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png" width="112" alt="gpt-image-2.5-flare product image"></a> |
| doubao-seedream-5-0-pro | 1K / default → 2048×2048 | $0.042857/image | **$0.042856** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg" width="112" alt="doubao-seedream-5-0-pro product image"></a> |

![8 models ordered by example amount](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/overview-en.jpg)

[Shared prompt, originals and cost sources](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/image-model-samples-2026-10-17/README.md) · [Pricing API](https://docs.toapis.com/docs/en/api-reference/account/pricing)

<!-- /TOAPIS-IMAGE-SAMPLES-20261017 -->

[English](README.md) · [中文](README_zh-CN.md) · [Pricing](PRICING.md) · [Charges](COSTS.md) · [Original outputs](GALLERY.md)



**$0.0019/image**: ToAPIs gpt-image-2-vip / low / 1K actual charge per VIP image, matching this test key’s catalog. A new async provider for the real wuyoscar/GPT-Image2-Skill CLI. On 2026-10-13 we completed **3 image-2(vip) generations/edits plus 1 standard control**, covering a product visual, an isometric scene and a reference edit.



## Demo



![Real outputs and CLI guide](screenshots/en/01-cover.png)



![Original reference edit](screenshots/en/03-reference.png)



Actual total **4.14 credits=$0.0207**. The account owner confirmed 0.38 credits per VIP image and 3 credits for the standard image; 1 credit=$0.005. API billing is still absent; provenance is retained separately. [Itemized charges](COSTS.md).



## Reproduce: dry-run first, explicit live call second



Python 3.11+ and Git; tested Python3.12, openai3.29.0 and python-dotenv1.2.4. Sparse checkout retrieves CLI/tests without the full gallery. This is a community patch and guide, not an official upstream edition or proof of a partnership.



```bash

git clone https://github.com/ToAPIs-2025/cheaper-gpt-image2-skill-toapis.git

git clone --filter=blob:none --no-checkout https://github.com/wuyoscar/GPT-Image2-Skill.git gpt-image-upstream

git -C gpt-image-upstream sparse-checkout init --cone

git -C gpt-image-upstream sparse-checkout set src tests skills/gpt-image/scripts

git -C gpt-image-upstream checkout 9f8aa1a44a4a5c0f5a5d6e45eed564b3e2d5b87f

cd cheaper-gpt-image2-skill-toapis

git -C ../gpt-image-upstream apply ../cheaper-gpt-image2-skill-toapis/adapter.patch

python -m venv .venv

# Windows: .venv\Scripts\activate

# macOS/Linux: source .venv/bin/activate

python -m pip install -r requirements-demo.txt

python -m pip install -e ../gpt-image-upstream

cp .env.example .env

# Windows PowerShell: Copy-Item .env.example .env

# Configure TOAPIS_API_KEY privately; never paste it into posts.

python run_cases.py --upstream ../gpt-image-upstream

python tests/test_adapter.py --upstream ../gpt-image-upstream

python tests/run_upstream_tests.py --upstream ../gpt-image-upstream

python run_cases.py --upstream ../gpt-image-upstream --key-file .env --live --case vip-product

```



The first live command generates one image. Keep the saved outputs and private-state receipts. If no task ID is returned, reconcile Task Logs before another POST. The next command runs all four cases; completed evidence is skipped, and existing submitted tasks reuse their IDs.



```bash

python run_cases.py --upstream ../gpt-image-upstream --key-file .env --live

```



The four-case catalog estimate is $0.0207. The runner reads current rates and stops if its estimate exceeds the separate $0.10 sub-cap. Generate the first case before the reference edit; reuse any saved output with the next CLI -i input.



## Reuse the upstream CLI directly



```bash

gpt-image --provider toapis --model gpt-image-2-vip \

  --quality low --resolution 1K --size square \

  -p "A fictional cobalt-blue perfume bottle on travertine, no text or logo" \

  -f result.png --dry-run

# Remove --dry-run only when ready for a paid generation.

gpt-image --provider toapis --model gpt-image-2-vip \

  --quality low --resolution 1K --size square \

  -p "Move the reference bottle to a sunlit botanical studio, no text or logo" \

  -i result.png -f edited.png

```



The second command is a paid edit example; generate result.png and check rates first. You can also use python -m gpt_image_cli.cli or the local skill launcher. Only launcher --help was checked; no full Claude/Codex/OpenClaw agent workflow was run. A remote uvx install of the unpatched upstream does not include this ToAPIs provider.



## Protocol differences and minimal patch



Pinned upstream SHA:  `9f8aa1a44a4a5c0f5a5d6e45eed564b3e2d5b87f`.



Modify src/gpt_image_cli/cli.py and add src/gpt_image_cli/toapis.py. The default OpenAI route remains; --provider toapis selects the adapter. Original call_generate, call_edit and write_outputs execute. Async output bytes are wrapped into the CLI’s existing b64_json shape and saved unchanged.



| Contract | ToAPIs behavior |

|---|---|

| Origin/auth | https://toapis.cn or https://toapis.com; normalize optional /v1; Bearer Key |

| Model | gpt-image-2-vip + low, or gpt-image-2 without quality |

| Size | CLI 1024x1024 → size 1:1; resolution 1K; actual pixels recorded separately |

| References | POST /v1/uploads/images → reference_images:[URL] |

| Submit | POST /v1/images/generations → persist id; generation POST not retried |

| Query | GET /v1/images/generations/{id}; 8s polling, 600s limit |

| Output | result.data[0].url → credential-free download → b64_json → original writer |



This route supports n=1, opaque PNG and the two listed models. It rejects masks, input_fidelity, JPEG/WebP output, compression/user and other models. The original moderation flag has no mapped control and is omitted. Resolution is a tier, not an exact pixel guarantee. Other sizes/tiers have validation, but only 1:1/1K was tested live.



## Verification and evidence



8 adapter offline tests and 18 original-project offline tests passed. For Windows SDK3 fixtures that clear the environment, the harness creates a trusted system SSL context beforehand; it does not disable TLS verification. Four live CLI calls completed. The first wrapper run hit an output-encoding issue after generation; its task and image were retained and the original ID reused without a second generation POST. Its short recovery timing is not generation latency.



[Prompts](cases/briefs.json) · [Task IDs, requests, hashes](evidence/runs.json) · [Sanitized CLI logs](evidence/vip-reference-edit-cli.txt)



## Upstream attribution and API access



[wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) · [Fixed source](https://github.com/wuyoscar/GPT-Image2-Skill/tree/9f8aa1a44a4a5c0f5a5d6e45eed564b3e2d5b87f) · [MIT license](LICENSE). Preserve upstream notices. All case prompts are original; no upstream gallery artwork is republished.



[Explore the ToAPIs image API and prices](https://go2v.toapis.com/1013_gptskill_cheaper_gh_en) · [X screenshot reuse](SCREENSHOT_GUIDE.md)

