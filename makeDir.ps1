if ($args.Count -lt 1) {
    write-host 'A numeric parameter is required'
    exit
}
     

$param1 = $args[0]
$dir = '.\day' + $param1
$inputFile = $dir + '\input.txt'
$inputTest = $dir + '\inputTest.txt'
$solutionFile = $dir + '\solution.py'
New-Item -Path $dir -ItemType Directory
New-Item $inputFile
New-Item $inputTest
New-Item $solutionFile