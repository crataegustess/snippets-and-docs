# The joy of BOMs

Frequently when something doesn't work, there's nothing obviously changed in a file but you're suddenly seeing `Invalid symbol` on line 1: it's a BOM (byte order mark). This is one of the annoying invisible characters that can wreck automated processing and testing. 

They can turn up more frequently during merges and in teams where some work on windows and some on macos or linux.

There's a number of ways of testing for them:

- open the file in a hex editor
  - mac: [hex fiend](http://ridiculousfish.com/hexfiend/) is good on a mac
  - windows: Notepadd ++ has a good hex viewer plugin
- (windows) open the file in Notepad++ and check encoding
- run a grep in the project folder (with the -p flag on gnu/linux but not on a mac): `grep -rn $'\xFEFF' *` or `grep -rl $'\xEF\xBB\xBF' .`

Some examples on stack overflow suggest setting a function and then calling it for a specific file. This is the mac compatible version:

```bash
$ has_bom() { head -c3 "$1" | grep -q $'\xef\xbb\xbf'; }
$ has_bom file && echo yes
yes
```

There's even a [oneliner](https://stackoverflow.com/questions/204765/elegant-way-to-search-for-utf-8-files-with-bom) to fix it (use at your own risk!)

```bash
find . -type f -exec sed '1s/^\xEF\xBB\xBF//' -i {} \;
```
