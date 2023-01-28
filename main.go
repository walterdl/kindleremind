package main

import (
	"kindleremind/clippings"
	"kindleremind/utils"
)

func main() {
	clippings := clippings.GetClippings()
	utils.JsonPrint(clippings)
}
