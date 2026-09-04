# SandboxKit

> Describe and validate conservative isolated-execution policies.

SandboxKit provides small helpers for working with sandbox profile metadata and resource policies. It focuses on policy inspection rather than executing untrusted code.

## Features

- Normalize sandbox profile metadata
- Compare resource limits
- Validate conservative policy fields
- Produce structured policy information
- Keep policy analysis local

## Workflow

```text
sandbox profile
      ↓
normalize
      ↓
validate
      ↓
compare limits
      ↓
policy review
```

## Example

```python
from sandboxkit import validate_profile

result = validate_profile(profile)
print(result)
```

See the implementation and tests for the supported profile schema.

## Scope

SandboxKit does **not** execute supplied code or claim to provide a complete security sandbox. It is a policy-analysis utility.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu