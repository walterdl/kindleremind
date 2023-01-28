package clippings

import "strings"

func splitByMetadata(s string) (string, string) {
	metadata := ""

	for {
		if indexOfLineBreak(s) != -1 {
			before := s[:indexOfLineBreak(s)]

			if metadata == "" {
				metadata = before
				s = deleteLineBreak(s)
				continue
			}

			if indexOfLineBreak(s) == 0 {
				s = deleteLineBreak(s)
			} else {
				break
			}
		} else {
			break
		}
	}

	return metadata, s
}

func indexOfLineBreak(s string) int {
	return strings.Index(s, lineBreak)
}

func deleteLineBreak(s string) string {
	s = s[indexOfLineBreak(s):]
	s = s[len(lineBreak):]

	return s
}
