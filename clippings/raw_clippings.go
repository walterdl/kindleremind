package clippings

import (
	"os"
	"strings"
)

func rawClippings() []string {
	f := readFile()

	return clearEmptyLastClipping(
		splitClippings(f),
	)
}

func readFile() string {
	content, err := os.ReadFile("My Clippings.txt")

	if err != nil {
		panic(err)
	}

	return string(content)
}

func splitClippings(s string) []string {
	return strings.Split(s, "==========")
}

func clearEmptyLastClipping(s []string) []string {
	if s[len(s)-1] == lineBreak {
		return s[:len(s)-1]
	}

	return s
}
