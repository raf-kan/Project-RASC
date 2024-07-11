package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("python3", "-c", "import pythonfile; print (pythonfile.cat_strings('foo', 'bar'))")
	fmt.Println(cmd.Args)
	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(out))
}
