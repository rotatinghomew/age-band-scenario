# age-band-scenario

联赛分组规程、共享领队和确认通知。 其中人物代号、机构、交易及历史回执均为合成资料。

## 数据约定

`data/layout.json` 逐一解释业务表及 CSV 列顺序，`data/rules.json` 记录运营口径。CSV 使用 UTF-8、首行为列名；空白字段表示未提供或不适用，`+` 隔开多值字段。历史记录的业务时刻与送交时刻含义不同，按各表说明解释。

- `entries.csv`：已开放与确认的赛项时段。
- `members.csv`：报名当时的候选资料，turns 是本人可到的日次。
- `choices.csv`：原始意向、通知和结局，2026 场次的未来结局单独见后续通知。
- `offers.csv`：新规程拟开放时段及共享场地；组席位还受该安排实际时段约束。
- `notices.csv`：事业部门分批回传的原位、替代位置和响应。
- `migration_requests.csv`：原场签认人与联赛队提出的互为前提请求，may_withdraw 仅描述该队能否撤回请求。
- `migration_replies.csv`：队员本人同意、撤回，或原场有权人签释；只指明本次确实回应的申请。
- `announced_groups.csv`：实际已通知成立的旧组与保留人数；核对按报名时已确认人数，不从模拟使用人数倒推。

## 本地检查

使用 Python 3.11 及标准库。`python3 inspect_inputs.py` 读取原始资料并列出记录数；`python3 -m unittest discover -s tests` 检查输入资料。检查不计算或发布业务结论。
