// Referenced Assemblies.
.assembly extern mscorlib
{
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) 
  .ver 4:0:0:0
}

// Our assembly.
.assembly example
{
  .hash algorithm 0x00008004
  .ver 0:0:0:0
}

.module example.exe

// Definition of Program class.
.class private auto ansi beforefieldinit Program
  extends [mscorlib]System.Object
{
    .method private hidebysig static void Main(string[] args) cil managed
    {
    .locals (
       [0]  int32 n10,
       [1]  int32 n20,
       [2]  int32 n30,
       [3]  int32 e10,
       [4]  bool e20,
       [5]  float32 e30,
       [6]  int32 U0001f60aU0001f922u4e2du65870,
       [7]  int32 read0,
       [8]  int32 empty0,
       [9]  bool b0,
       [10]  int32 i0,
       [11]  float32 temp0,
       [12]  int32 _0     )
   .entrypoint
   //.maxstack  8
   ldloca    n10
   ldc.i4    1
   stind.i4
   ldloca    n20
   ldc.i4    2
   stind.i4
   ldloca    n30
   ldc.i4    3
   stind.i4
   call    string [mscorlib]System.Console::ReadLine()
   call int32 [mscorlib]System.Int32::Parse(string)
   stloc read0
   ldloca    empty0
   ldc.i4    1
   stind.i4
   ldloc    empty0
   ldc.i4    10
   ceq
   brfalse    m1
   ldloc    empty0
   call void [mscorlib]System.Console::WriteLine(int32)
   br    m2
m1:
   ldloc    empty0
   ldloc    read0
   ceq
   ldc.i4.0
   ceq
   brfalse    m3
   ldc.i4    100
   neg
   ldloc    read0
   cgt
   ldc.i4.0
   ceq
   call void [mscorlib]System.Console::WriteLine(int32)
   ldloc    read0
   ldc.i4    100
   cgt
   ldc.i4.0
   ceq
   call void [mscorlib]System.Console::WriteLine(int32)
   ldc.i4    50
   ldloc    read0
   clt
   call void [mscorlib]System.Console::WriteLine(int32)
   ldloc    read0
   ldc.i4    60
   clt
   call void [mscorlib]System.Console::WriteLine(int32)
   ldc.i4    50
   ldc.i4    50
   cgt
   call void [mscorlib]System.Console::WriteLine(int32)
   ldc.i4    50
   ldc.i4    50
   clt
   ldc.i4.0
   ceq
   call void [mscorlib]System.Console::WriteLine(int32)
   ldloca    b0
   ldc.i4    1
   stind.i4
   ldloca    b0
   ldc.i4    0
   stind.i4
m4:
   ldloc    b0
   ldc.i4    1
   ceq
   ldc.i4.0
   ceq
   brfalse    m5
   ldloca    i0
   ldc.i4    0
   stind.i4
   br    m6
m6:
   ldloc    i0
   ldc.i4    100
   clt
   brfalse    m9
   br    m7
m8:
   ldloca    i0
   ldloc    i0
   ldc.i4    1
   add
   stind.i4
   br    m6
m7:
   ldloc    i0
   ldloc    read0
   ceq
   brfalse    m10
   ldloca    b0
   ldc.i4    1
   stind.i4
   br    m11
m10:
m11:
   br    m8
m9:
   br    m4
m5:
   ldloca    temp0
   ldc.i4    10
   conv.r4
   ldc.i4    2
   conv.r4
   mul
   ldc.i4    3
   conv.r4
   ldc.i4    20
   ldloc    read0
   add
   conv.r4
   div
   ldloc    read0
   conv.r8
   call   float64 [mscorlib]System.Math::Pow(float64, float64)
   add
   stind.r4
   ldloc    temp0
   call void [mscorlib]System.Console::WriteLine(float32)
   ldc.i4    2
   ldc.i4    2
   ldc.i4    3
   conv.r8
   call   float64 [mscorlib]System.Math::Pow(float64, float64)
   call   float64 [mscorlib]System.Math::Pow(float64, float64)
   call void [mscorlib]System.Console::WriteLine(float32)
   ldc.i4    2
   ldc.i4    2
   conv.r8
   call   float64 [mscorlib]System.Math::Pow(float64, float64)
   ldc.i4    3
   conv.r4
   conv.r8
   call   float64 [mscorlib]System.Math::Pow(float64, float64)
   call void [mscorlib]System.Console::WriteLine(float32)
   ldc.i4    2
   ldc.i4    2
   ldc.i4    3
   conv.r8
   call   float64 [mscorlib]System.Math::Pow(float64, float64)
   call   float64 [mscorlib]System.Math::Pow(float64, float64)
   call void [mscorlib]System.Console::WriteLine(float32)
   ldloca    _0
   ldc.i4    0
   stind.i4
   br    m12
m12:
   ldloc    _0
   ldc.i4    1
   cgt
   ldc.i4.0
   ceq
   brfalse    m15
   br    m13
m14:
   ldloca    _0
   ldloc    _0
   ldc.i4    1
   add
   stind.i4
   br    m12
m13:
   br    m14
m15:
   br    m2
m3:
   ldloc    empty0
   call void [mscorlib]System.Console::WriteLine(int32)
   br    m2
m2:
	ret    
}
}