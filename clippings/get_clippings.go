package clippings

import (
	"strings"
)

const lineBreak = "\r\n"
const endOfTitle = "\r\n- "

func GetClippings() []Clipping {
	result := make([]Clipping, 0)

	for _, c := range rawClippings() {
		// Trims BOM character
		c = trimPrefix(c, string(rune('\uFEFF')))
		c = trimPrefix(c, lineBreak)
		c = trimSuffix(c, lineBreak)
		t, c := abstractTitle(c)
		m, c := abstractMetadata(c)

		if isMarker(m) {
			continue
		}

		result = append(result, Clipping{
			Title:    t,
			Metadata: m,
			Content:  c,
		})
	}

	return result
}

func isMarker(metadata string) bool {
	return strings.HasPrefix(metadata, "El marcador en la posición")
}
