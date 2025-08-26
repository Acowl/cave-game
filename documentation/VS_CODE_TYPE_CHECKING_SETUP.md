# VS Code Python Type Checking Setup Guide

## Enabling Type Checking in VS Code

To enable Python type checking in Visual Studio Code as suggested in the feedback, follow these steps:

### Method 1: VS Code Settings UI
1. Open VS Code Settings (Ctrl+, or Cmd+,)
2. Search for "python type checking"
3. Find "Python › Analysis: Type Checking Mode"
4. Change from "off" to "basic" or "strict"

### Method 2: Settings JSON
Add this to your VS Code settings.json:
```json
{
    "python.analysis.typeCheckingMode": "basic"
}
```

### Method 3: Workspace Settings
Create `.vscode/settings.json` in your project:
```json
{
    "python.analysis.typeCheckingMode": "strict",
    "python.analysis.autoImportCompletions": true,
    "python.analysis.completeFunctionParens": true
}
```

## Type Checking Modes

- **off**: No type checking (default)
- **basic**: Basic type checking, reports obvious type errors
- **strict**: Comprehensive type checking, reports all type issues

## Benefits After Enabling

With type checking enabled, VS Code will:
- Show red squiggly lines for type errors
- Display errors in the Problems panel (Ctrl+Shift+M)
- Provide better IntelliSense and autocompletion
- Catch issues like missing parameters in Scene initialization
- Warn about undefined attributes like `current_scene.name`

## Additional Recommendations

1. **Install Pylance extension** (usually included with Python extension)
2. **Use mypy for command-line type checking**:
   ```bash
   pip install mypy
   mypy your_file.py
   ```
3. **Consider using @dataclass for better type safety**:
   ```python
   from dataclasses import dataclass
   
   @dataclass
   class Scene:
       name: str
       description: str
       exits: Dict[str, str]
       locked: bool = False
       key: Optional[str] = None
   ```

The type checking would have caught the issues mentioned in the feedback:
- Missing Scene constructor parameters
- Undefined `current_scene.name` attribute
- Missing inventory methods

All these issues have now been fixed in the codebase!
