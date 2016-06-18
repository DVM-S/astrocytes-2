# STYLE

1. Each component must be in a separate class, in a separate file
2. Each component must have a `render` method.
  1. The `render` method must only be concerned with rendering the component and nothing else.
  2. If data manipulation is needed, separate method must be created and called.
3. In each component class, member functoins must be placed alphabetically. The `render` method must be placed at the bottom.
4. Any sub-render method (ex: `render_button`, `render_title` etc) must be placed before render, in alphabetically.
