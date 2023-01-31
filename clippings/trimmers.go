package clippings

import "strings"

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
