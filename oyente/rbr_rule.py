#Pablo Gordillo

'''
RBRRule class represents the rules of the transaction system.
Each rule contains:
 * identifier

'''

class RBRRule:
    def __init__(self,blockId,typeBlock):
        self.blockId = blockId

        if typeBlock == "block":
            self.rule_name = "block"+str(blockId)
        else:
            self.rule_name = "jump"+str(blockId)

        self.arg_input = 0
        self.arg_global = 0
        self.arg_local = []
        self.arg_ret = []
        self.guard=""
        self.instr=[]
        self.rbr_type = typeBlock
        self.bc = ["address","balance","origin","caller","callvalue","calldataload","calldatasize","calldatacopy",
                   "codesize","codecopy","gasprice","extcodesize","extcodecopy","mcopy","coinbase","number","difficulty",
                   "gaslimit","gas"] #To be extended
        
    def get_guard(self):
        return self.guard

    def set_guard(self, guard):
        self.guard = guard

    # def add_guard(self, guard):
    #     self.guard.append(guard)

    def get_Id(self):
        return self.blockId

    def set_Id(self, b_id):
        self.blockId = b_id

    def get_instructions(self):
        return self.instr

    def set_instructions(self, instr):
        self.instr = instr

    def add_instr(self, instr):
        self.instr.append(instr)

    def get_type(self):
        return self.rbr_type

    def get_rule_name(self):
        return self.rule_name

    def write_rule(self, fd):
        pass

    def get_index_invars(self):
        return self.arg_input

    def set_index_input(self,num):
        self.arg_input = num

    def get_args_local(self):
        return self.arg_local

    def set_args_local(self,ls):
        self.arg_local = ls

    def add_arg_local(self,l):
        if l not in self.arg_local:
            self.arg_local.append(l)

    def set_global_arg(self,val):
        self.arg_global = val

    def get_global_arg(self):
        return self.arg_global

    def get_ret_var(self):
        return arg_ret

    def set_ret_var(self,var):
        self.arg_ret = var

    def build_bc_vars(self):
        #Todo: get only those that are used in this contract
        instr = self.bc
        return ", ".join(instr)

    def build_input_vars(self):
        in_vars = []
        for i in xrange(self.arg_input-1,-1,-1):
            var = "s("+str(i)+")"
            in_vars.append(var)
        return in_vars

    def build_field_vars(self):
        field_vars = []
        for i in xrange(0,self.arg_global+1):
            var = "g("+ str(i)+")"
            field_vars.append(var)
        return field_vars

    def display(self):
        
        new_instr = filter(lambda x: x !="",self.instr) #clean instructions ""

        arg_input = self.build_input_vars()

        bc_input = self.build_bc_vars()
        
        if (arg_input == []):
            print self.rule_name+"("+str(self.arg_global)+", bc"+")=>"
        else:
            print self.rule_name+"(" + ", ".join(arg_input) + ", " + str(self.arg_global) + ", "+ str(self.arg_ret) +")=>"

        if self.guard != "" :
            print "\t"+self.guard

        for instr in new_instr:
            print "\t"+instr
