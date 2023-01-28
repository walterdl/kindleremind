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

	for _, c := range rawClippings {
		c = trimLeadingLineBreak(c)
		t, c := abstractTitle(c)
		m, c := abstractMetadata(c)
		c = trimEndingLineBreaks(c)

		result = append(result, Clipping{
			Title:    t,
			Metadata: m,
			Content:  c,
		})
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

func trimLeadingLineBreak(s string) string {
	return strings.TrimPrefix(s, lineBreak)
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

func trimEndingLineBreaks(s string) string {
	for {
		i := strings.LastIndex(s, lineBreak)

		if i == -1 {
			return s
		}

		s = s[:i]
	}
}
