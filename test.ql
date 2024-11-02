var x: Int = 10
for i in 0...5 {
    var x:Float = 1.5
    // Float error
    for i in x+5..<10 {
        var x = 10
        print(i)
    }
}
