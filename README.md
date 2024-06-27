# Versioning tool for REMLA frontend

Versoning tool for the [app frontend](https://github.com/remla24-team-1/app).

If you wish to test the package, you can install it locally through `$ pip install remlaversionutilpy`. You can also install it by running `poetry install` from within the lib-version folder.

## Example usage
```
# python
from remlaversionutilpy import *
print(VersionUtil.get_version())
```

## Release instructions

To release an updated version, set the version variable within the `pyproject.toml` and push a tag with the same version number. For example, to release VX.X.X, set `version = X.X.X` in `pyproject.toml`. Then add the new tag through `git tag VX.X.X` and push the tag using `git push origin tag VX.X.X`. The new version will be automatically published to PyPI by the github workflow.
