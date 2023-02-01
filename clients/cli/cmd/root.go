package cmd

import (
	"github.com/spf13/cobra"
	"github.com/walterdl/kindleremind/clippings"
	"github.com/walterdl/kindleremind/utils"
)

var (
	rootCmd = &cobra.Command{
		Use:   "kindleremind",
		Short: "Kindle Remind is a tool to remind you of your Kindle clippings",
		Long: `Given a clippings file from your kindle (usually "My Clippings.txt"),
this tool abstracts every clipping from the file and uploads them in your
personal AWS environment. Then, it will send you a reminder every day with
the clippings you have read via email.`,
		Version: "0.0.1",
		RunE:    runCommand,
	}

	file string
)

func init() {
	rootCmd.Flags().StringVarP(&file, "file", "f", "./My Clippings.txt", "File path to your clippings file")
}

func Execute() error {
	return rootCmd.Execute()
}

func runCommand(cmd *cobra.Command, args []string) error {
	clippings, err := clippings.GetClippings(file)
	if err != nil {
		return err
	}

	utils.JsonPrint(clippings)
	return nil
}
