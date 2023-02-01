package utils

import (
	"encoding/json"
	"fmt"
)

func JsonPrint(v interface{}) {
	val, err := json.MarshalIndent(v, "", "  ")

	if err != nil {
		fmt.Println("Error marshalling JSON: ", err)
	}

	fmt.Println(string(val))
}
