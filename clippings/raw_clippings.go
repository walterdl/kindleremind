package clippings

import (
	"os"
	"strings"
)

func getRawClippings(file string) ([]string, error) {
	f, err := readFile(file)

	if err != nil {
		return nil, err
	}

	return clearEmptyLastClipping(
		splitClippings(f),
	), nil
}

func readFile(file string) (string, error) {
	content, err := os.ReadFile(file)

	if err != nil {
		return "", err
	}

	return string(content), nil
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
