# **T**est **D**riven **D**evelopment (and Pairing)

## Where's the value?

- more robust code
- confirmation of expected behaviour before diving into code
- tests document code (though hopefully not too fragile)
- protects against feature corruption or loss when context switching (green tests ~ feature complete)

and when mixed with pairing
- instant knowledge share
- excludes 'works on my machine' factor (especially if remote and checking into git on handover)

## Pairing techniques:

- ping pong (1 driver, 1 navigator)
  - write a failing test
  - pass to next driver
  - write code, check green, refactor, (write failing test)

- time boundary (1 driver, 1 navigator)
  - 8 or 15 min timer
  - handover when timer goes
  - expect first few cycles to be set up if first time on project

- mobs (1 driver, many navigators / researchers)
  - works best with 8 min timer
  - keep mob numbers small (4ish) to ensure everyone engaged
  - driver does not think!

## Making it slick

- tests should be able to be run and rerun quickly; scripts for automated testing for servers that include installation and virtual environment setup every time (pip, npm etc) will not work here. Go for single cli command or ide tools to run tests. Test on save in ides can sometimes work or can be annoying.

- practise makes everything better, the more cycles done (with more people if pairing) the slicker the handover.

- take a bit of time during refactor phase (red -> green -> **refactor**) to clean up tests. Many unit test frameworks allow for the same test function or method to be run with multiple test data sets (or test cases) via decorators; this can help keep your test code DRY if it's getting too unreadable.
  - python
    - [py test params](https://docs.pytest.org/en/latest/parametrize.html)
    - [nose test params](https://github.com/wolever/parameterized)
  - c sharp
    - [nunit testcase attribute](https://github.com/nunit/docs/wiki/TestCase-Attribute)
    - [nunit testcase data](https://github.com/nunit/docs/wiki/TestCaseData)
  - javascript:
    - [dynamically generated](https://mochajs.org/#dynamically-generating-tests)
    - [mocha param](https://github.com/mikejsdev/mocha-param)
  - [junit does it for java](https://github.com/junit-team/junit4/wiki/Parameterized-tests)



