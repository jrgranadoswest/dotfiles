return {
    "nvim-telescope/telescope.nvim",

    tag = "0.1.5",

    dependencies = {
        "nvim-lua/plenary.nvim"
    },

    config = function()
        require('telescope').setup({})

        local builtin = require('telescope.builtin')
	
	-- project file
        vim.keymap.set('n', '<leader>pf', builtin.find_files, {})
	
	-- git file search (only look at files in git, e.g. ignore node_modules)
        vim.keymap.set('n', '<C-g>', builtin.git_files, {})
	
	-- project search
        vim.keymap.set('n', '<leader>ps', function()
		-- fuzzy finder
            builtin.grep_string({ search = vim.fn.input("Grep > ") })
        end)
    end
}
