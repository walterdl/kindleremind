package clippings

import (
	"strings"
)

const lineBreak = "\r\n"
const endOfTitle = "\r\n- "

func GetClippings(file string) ([]Clipping, error) {
	result := make([]Clipping, 0)

	clippings, err := getRawClippings(file)
	if err != nil {
		return nil, err
	}

	for _, c := range clippings {
		c = clearClipping(c)
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

	return result, nil
}

func clearClipping(c string) string {
	// Trims BOM character
	c = trimPrefix(c, string(rune('\uFEFF')))
	c = trimPrefix(c, lineBreak)
	c = trimSuffix(c, lineBreak)

	return c
}

func isMarker(metadata string) bool {
	return strings.HasPrefix(metadata, "El marcador en la posición")
}
