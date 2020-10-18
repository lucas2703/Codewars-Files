def simple_assembler(program):
    i = 0
    register = {}
    while i < len(program):
        inst = program[i].split(' ')
        # add to register
        if inst[1] not in register:
            register[inst[1]] = 0
        if inst[0] == 'mov':
            if inst[2].isalpha():
                register[inst[1]] = register[inst[2]]
            else:
                register[inst[1]] = int(inst[2])
        elif inst[0] == 'inc':
            register[inst[1]]+= 1
        elif inst[0] == 'dec':
            register[inst[1]] -= 1
        if inst[0] == 'jnz':
            if register[inst[1]] != 0:
                i  += int(inst[2])
            else:
                i += 1
        else:
            i += 1
                
            
    return register