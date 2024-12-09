def saveCIL(file_name, table_of_vars, postfix_code):
    def get_il_type(var_name):
        var_type = table_of_vars.get(var_name)
        types_map = {
            'floatnum': 'float32',
            'intnum': 'int32',
            'boolval': 'bool'
        }
        return types_map.get(var_type, '')

    def generate_local_var(index, var_name):
        il_type = get_il_type(var_name)
        return f"       [{index}]  {il_type} {var_name}"

    def generate_code():
        code_lines = []
        current_label = None
        prev_type = ''
        prev_var = ''

        for index, (token, token_type) in enumerate(postfix_code):
            if token_type in ('jump', 'jf', 'colon'):
                if token_type == 'jump':
                    code_lines.append(f"   br    {current_label}")
                elif token_type == 'jf':
                    code_lines.append(f"   brfalse    {current_label}")
                elif token_type == 'colon':
                    code_lines.append(f"{current_label}:")
                current_label = None

            elif token_type == 'label':
                current_label = token

            elif token_type in ('l-val', 'r-val'):
                var_type = table_of_vars[token]
                prev_type = {'intnum': 'int', 'floatnum': 'float'}.get(var_type, 'bool')

                is_readline = index + 1 < len(postfix_code) and postfix_code[index + 1][1] == 'readline'
                prev_var = token

                if token_type == 'l-val' and not is_readline:
                    code_lines.append(f"   ldloca    {token}")
                elif token_type == 'r-val':
                    code_lines.append(f"   ldloc    {token}")

            elif token_type == 'intnum':
                code_lines.append(f"   ldc.i4    {token}")
                if prev_type == 'float':
                    code_lines.append("   conv.r4")
                prev_type = 'int'

            elif token_type == 'floatnum':
                # if prev_type == 'int':
                #     code_lines.append("   conv.r4")
                code_lines.append(f"   ldc.r4    {token}")
                prev_type = 'float'

            elif token_type == 'assign_op':
                code_lines.append(f"   stind.{('i4' if prev_type in ('int', 'bool') else 'r4')}")

            elif token_type == 'print':
                type_map = {'int': 'int32', 'float': 'float32'}.get(prev_type, prev_type)
                code_lines.append(f'   call void [mscorlib]System.Console::WriteLine({type_map})')
                prev_type = ''

            elif token_type == 'readline':
                code_lines.append("   call    string [mscorlib]System.Console::ReadLine()")
                type_map = {'int': 'Int32', 'float': 'Single'}.get(prev_type, 'Int32')
                code_lines.append(f'   call {prev_type}32 [mscorlib]System.{type_map}::Parse(string)')
                code_lines.append(f'   stloc {prev_var}')
                prev_type = ''

            elif token_type == 'rel_op':
                code_lines.append({
                                      '>': "   cgt",
                                      '<': "   clt",
                                      '>=': "   clt\n   ldc.i4.0\n   ceq",
                                      '<=': "   cgt\n   ldc.i4.0\n   ceq",
                                      '==': "   ceq",
                                      '!=': "   ceq\n   ldc.i4.0\n   ceq"
                                  }.get(token, ''))

            elif token_type in ('mult_op', 'add_op'):
                operation = {
                    '+': "   add",
                    '-': "   sub",
                    '*': "   mul",
                    '/': "   div",
                    'NEG': "   neg"
                }.get(token, '')
                if token in ('*', '/') and prev_type == 'int':
                    code_lines.append("   conv.r4")
                    prev_type = 'float'
                code_lines.append(operation)

            elif token_type == 'power_op':
                if prev_type == 'int':
                    code_lines.append('   conv.r8')
                code_lines.append("   call   float64 [mscorlib]System.Math::Pow(float64, float64)")
                prev_type = 'float'

            elif token_type == 'boolval':
                code_lines.append(f"   ldc.i4    {int(token == 'true')}")
                prev_type = "bool"
        return "\n".join(code_lines)

    fname = file_name + ".il"
    header = f"""// Referenced Assemblies.
.assembly extern mscorlib
{{
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) 
  .ver 4:0:0:0
}}

// Our assembly.
.assembly {file_name}
{{
  .hash algorithm 0x00008004
  .ver 0:0:0:0
}}

.module {file_name}.exe

// Definition of Program class.
.class private auto ansi beforefieldinit Program
  extends [mscorlib]System.Object
{{
    .method private hidebysig static void Main(string[] args) cil managed
    {{
    .locals (
"""

    local_vars = ",\n".join([generate_local_var(i, var) for i, var in enumerate(table_of_vars)]) + "     )"

    code = generate_code()
    entrypoint = "\n   .entrypoint\n   //.maxstack  8\n"

    with open(fname, 'w', encoding="utf-8-sig") as f:
        f.write(header + local_vars + entrypoint + code + "\n\tret    \n}\n}")

    print(f"IL-program for CLR saved in file {fname}")
