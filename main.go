package main

import (
	"github.com/walterdl/kindleremind/clippings"
	"github.com/walterdl/kindleremind/utils"
)

func main() {
	clippings := clippings.GetClippings()
	utils.JsonPrint(clippings)
}
