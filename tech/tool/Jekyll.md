# Jekyll
#tech/tool
## How to escape liquid template tags?

There _is_ a way to escape without plugins, use the code below:

```
{{ "{% this " }}%}
```

and for tags, to escape `{{ this }}` use:

```
{{ "{{ this " }}}}
```