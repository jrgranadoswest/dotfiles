vim.opt.guicursor = ""

-- line number & relative line numbers
vim.opt.number = true
vim.opt.relativenumber = true

vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true

-- prevent line wrapping
vim.opt.wrap = false

-- don't do backups, but give undotree long term
vim.opt.swapfile = false
vim.opt.backup = false
vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
vim.opt.undofile = true

-- incremental search, but don't keep highlighted after
vim.opt.hlsearch = false
vim.opt.incsearch = true


-- when scrolling, show at least this many lines from cursor
vim.opt.scrolloff = 5

vim.opt.colorcolumn = "100"
