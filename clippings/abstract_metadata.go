package clippings

import (
	"strings"
)

func abstractMetadata(s string) (string, string) {
	if i := indexOfLineBreak(s); i != -1 {
		metadata := s[:i]
		content := s[i:]
		content = trimPrefix(content, lineBreak)

		if content == "" {
			content = metadata
		}

		return metadata, content
	}

	return "", s
}

func indexOfLineBreak(s string) int {
	return strings.Index(s, lineBreak)
}
