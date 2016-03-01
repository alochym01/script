-- Kamailio Lua Config
require 'ngcp.ngcp'

function ngcp_init()
    if not ngcp then
    	sr.log("dbg", "creating ngcp object\n")
        ngcp = NGCP:new()
        loaded_keys = {caller={}, callee={}}
        -- set config
        ngcp.config.db_user = "kamailio"
        ngcp.config.db_pass = "Xjcgr3jyhwRjjfnUhkoN"
        ngcp.config.db_host = "localhost"
        ngcp.config.db_port = "3306"
        ngcp.config.db_database = "kamailio"
        -- default values
        local temp_defaults = { "peer", "dom" }
        local _,v
        for _,v in ipairs(temp_defaults) do
            ngcp.config.default[v].sst_enable = "yes"
            ngcp.config.default[v].sst_expires = 300
            ngcp.config.default[v].sst_min_timer = 90
            ngcp.config.default[v].sst_max_timer = 7200
            ngcp.config.default[v].lbrtp_set = 50
        end
    end
end

function ngcp_clean(vtype, group)
    ngcp_init()
    ngcp:clean(vtype, group)
    if (group=='usr' or group=='dom') then
        ngcp:clean(vtype, 'real')
    end

end

function ngcp_caller_contract_load(contract)
    ngcp_init()
    ngcp:caller_contract_load(contract)
end

function ngcp_callee_contract_load(contract)
    ngcp_init()
    ngcp:callee_contract_load(contract)
end

function ngcp_caller_peer_load(peer)
    ngcp_init()
    ngcp:caller_peer_load(peer)
end

function ngcp_callee_peer_load(peer)
    ngcp_init()
    ngcp:callee_peer_load(peer)
end

function ngcp_caller_usr_load(uuid, dom)
    ngcp_init()
    ngcp:caller_usr_load(uuid, dom)
end

function ngcp_callee_usr_load(uuid, dom)
    ngcp_init()
    ngcp:callee_usr_load(uuid, dom)
end
--EOF
