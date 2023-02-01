package clippings

import (
	"strings"
)

func abstractMetadata(s string) (string, string) {
	if i := indexOfLineBreak(s); i != -1 {
		metadata := s[:i]
		content := s[i:]
		content = trimPrefix(content, lineBreak)

		return metadata, content
	}

	return s, ""
}

func indexOfLineBreak(s string) int {
	return strings.Index(s, lineBreak)
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
