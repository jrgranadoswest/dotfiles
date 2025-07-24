
-- vim.cmd 'colorscheme koehler'
-- vim.cmd 'colorscheme slate'
vim.o.background = "dark"
vim.cmd [[
    silent! colorscheme lunaperche
    hi Normal guibg=#000
]]

-- require remap.lua file inside the jrgw dir
require("jrgw.remap")
require("jrgw.set")
