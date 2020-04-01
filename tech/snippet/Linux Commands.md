# Linux Commands
#tech/snippet
execute the command with line number of 1957 in 'history' command:
`!1957`

how to count the number of lines of code in a directory recursively:
`find . -name '*.py'| xargs wc -l`

Way to unzip file to different directories:
``` bash
for i in *.zip; do 
	mkdir "$i-dir" 
	cd "$i-dir" 
	unzip "../$i" 
	cd ..
done
```

find string recursively in files in a folder:
`find . -type f -print0 | xargs -0 grep -l "try"`
find file recursively:
`find . -name "*.pdf"`
replace string recursively in files in a folder:
`find . -name "*.cpp" -print0 |  xargs -0 -n 1 sed -i -e 's/from/to/g'`
