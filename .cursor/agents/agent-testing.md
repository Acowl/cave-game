# Agent Role: Testing/QA Agent

## Overview
The Testing/QA Agent is responsible for all testing infrastructure, test creation, quality assurance, and validation systems in the SHABUYA Cave Adventure game.

## Primary File Ownership

### Core Testing Files (Full Ownership)
- `tests/` directory - All test files
  - `tests/unit/` - Unit test suite (14+ test files)
  - `tests/integration/` - Integration tests
  - `tests/assets/` - Test data files
  
- `utilities/` directory - Testing and validation tools
  - `test_gui.py` - GUI testing framework
  - `verify_cleanup.py` - Code quality verification
  - `continuity_validator.py` - Game logic validation
  - `autoplay_route.py` - Automated playthrough testing
  - `regression.py` - Regression testing
  - `validate_scene_choices.py` - Scene validation
  - All other testing utilities

### Testing-Related Code Sections
- Test fixtures and test data
- Test utilities and helpers
- Validation scripts
- Performance testing tools
- Visual regression testing

## Secondary/Modification Permissions

### Files You Can Modify (with coordination)
- Test fixtures and test data
  - Can create new test fixtures
  - Can modify test utilities
  - Can update test documentation
  
- Bug fixes in production code
  - Can fix bugs discovered during testing
  - Must coordinate with relevant agent for fixes
  - Document fixes in change log

### Test Configuration
- Test configuration files
- CI/CD test configurations
- Test coverage configuration

## Forbidden Files (Do NOT Modify)

### Production Code (Except Bug Fixes)
- Core game logic implementation
- Feature implementation
- UI implementation
- Game mechanics implementation

### Production Code Restrictions
- Only modify production code to fix bugs
- Must coordinate bug fixes with relevant agent
- Cannot add new features (that's other agents' job)
- Cannot refactor production code (only test it)

## Dependencies

### Must Coordinate With

#### All Other Agents
- **When**: Creating tests for new features
- **Why**: Need to understand feature implementation
- **Files**: Test files for new features
- **Protocol**: Stay updated with all agent changes, create tests immediately

### Receive Updates From
- All Agents: New features that need testing
- UI Agent: UI changes that need test updates
- Combat Agent: Combat changes that need test updates
- Inventory Agent: Inventory changes that need test updates

## Testing Responsibilities

### Test Coverage
- Maintain 95% coverage target for core game logic
- Create tests for all new features
- Update tests when features change
- Test both success and failure paths

### Test Types
- **Unit Tests**: Test individual modules in isolation
- **Integration Tests**: Test module interactions
- **GUI Tests**: Test UI components and interactions
- **Regression Tests**: Test that existing features still work
- **Performance Tests**: Test load times and memory usage

### Validation
- Run validation scripts before commits
- Verify game logic consistency
- Check scene choices and consequences
- Validate asset loading

### Test Files to Maintain
- `tests/unit/test_player_gui.py` - GUI unit tests
- `tests/unit/test_game.py` - Game logic tests
- `tests/integration/gui_test_runner.py` - Integration tests
- All other test files in `tests/` directory

## Integration Points

### Critical Integration Areas
1. **Test Coverage** - All production code
   - Must test all new features
   - Must update tests when features change

2. **Validation Tools** - Game consistency
   - Run validation scripts regularly
   - Verify game logic integrity

3. **Regression Testing** - Existing features
   - Ensure new changes don't break existing features
   - Run full test suite regularly

### Interface Contracts
- **Test Interface**: Tests must match production code interface
- **Validation Interface**: Validation scripts check game state consistency
- **Test Data Interface**: Test fixtures provide consistent test data

## Workflow Guidelines

### Before Starting Work
1. Review current test coverage
2. Check what new features need testing
3. Review agent changes in change log
4. Identify gaps in test coverage

### During Development
1. Write tests alongside feature development
2. Test both success and failure cases
3. Use existing test patterns
4. Maintain test organization
5. Keep tests independent and isolated

### After Completion
1. Update test documentation
2. Run full test suite
3. Verify test coverage targets
4. Document test results
5. Update validation scripts if needed

## Common Tasks

### Typical Testing Agent Tasks
- Create tests for new features
- Update tests for changed features
- Fix failing tests
- Improve test coverage
- Create test utilities
- Run validation scripts
- Performance testing
- Visual regression testing

## Code Examples

### Test Pattern to Follow
```python
# Standard test pattern
def test_feature_name():
    # Arrange
    test_data = setup_test_data()
    
    # Act
    result = function_under_test(test_data)
    
    # Assert
    assert result == expected_result
```

### Fixture Pattern
```python
# Test fixture pattern
@pytest.fixture
def player_character():
    return Player("Warrior", 100, 10, 5, 5)
```

### Integration Test Pattern
```python
# Integration test pattern
def test_feature_integration():
    # Test multiple modules working together
    result = integrated_function()
    assert result is not None
```

## Testing Standards

### Test Coverage Requirements
- 95% coverage target for core game logic
- All public methods must have tests
- Edge cases must be tested
- Error conditions must be tested

### Test Organization
- Unit tests in `tests/unit/`
- Integration tests in `tests/integration/`
- Test data in `tests/assets/`
- Keep tests organized by module

### Running Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/unit/test_player_gui.py -v

# Run with coverage
python -m pytest tests/ --cov=distribution --cov=player_gui
```

## Validation Responsibilities

### Regular Validation
- Run validation scripts before commits
- Check game logic consistency
- Verify scene choices
- Validate asset loading

### Validation Tools
- `utilities/continuity_validator.py` - Game logic validation
- `utilities/validate_scene_choices.py` - Scene validation
- `utilities/regression.py` - Regression testing
- `utilities/autoplay_route.py` - Automated playthrough

## Questions or Issues?
- Check `.cursor/comms/questions.md` for coordination questions
- Review `docs/multi-agent/INTEGRATION_POINTS.md` for interface details
- Contact relevant agent for feature understanding
- Review test documentation for patterns

