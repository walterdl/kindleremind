package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
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
	rootCmd.Flags().StringVarP(&file, "file", "f", "", "File path to your clippings file")
	rootCmd.MarkFlagRequired("file")
}

func Execute() error {
	return rootCmd.Execute()
}

func runCommand(cmd *cobra.Command, args []string) error {
	fmt.Println("Running command", file)

	return nil
}
