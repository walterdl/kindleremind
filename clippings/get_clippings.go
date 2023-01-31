package clippings

import (
	"os"
	"strings"
)

const lineBreak = "\r\n"
const endOfTitle = "\r\n- "

func GetClippings() []Clipping {
	rawClippings := clearEmptyLastClipping(splitClippings(getRawContent()))
	result := make([]Clipping, len(rawClippings))

	for i, c := range rawClippings {
		// Trims BOM character
		c = trimPrefix(c, string(rune('\uFEFF')))
		c = trimPrefix(c, lineBreak)
		c = trimSuffix(c, lineBreak)
		t, c := abstractTitle(c)
		m, c := abstractMetadata(c)

		result[i] = Clipping{
			Title:    t,
			Metadata: m,
			Content:  c,
		}
	}

	return result
}

func getRawContent() string {
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

func trimPrefix(s string, prefix string) string {
	for strings.HasPrefix(s, prefix) {
		s = strings.TrimPrefix(s, prefix)
	}

	return s
}

func trimSuffix(s string, suffix string) string {
	for strings.HasSuffix(s, suffix) {
		s = strings.TrimSuffix(s, suffix)
	}

	return s
}

func abstractTitle(s string) (title, rest string) {
	i := strings.Index(s, endOfTitle)

	if i == -1 {
		// No title found. Title is considered empty and the rest is the whole given string.
		rest = s
	} else {
		title = s[:i]
		rest = s[i:]
		// Removes the set of characters that ends the title
		rest = rest[len(endOfTitle):]
	}

	return
}
