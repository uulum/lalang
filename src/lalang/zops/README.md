
create array kosong
let mut body = Vec::new();

create array initialized data

== susah sekali hafal Optional Some None dan Result Ok Err
ini spt wieke vs gaia.

# TODO

new utk array, dict, set, dst.
termasuk hasilkan initialized array...

myarr = [1,2,3,4]
int[] myArray;
int[] myArray = {13, 14, 15};
int[] intArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int[] intArray = new int[10];
int[] intArray = new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
int[] intArray = new int[]{13, 14, 15};

int[] stringArray = {"zelda", "link", "ganon"};
int[] stringArray = new String[]{"zelda", "link", "ganon"};
public String[] getNames() {
  return new String[]{"zelda", "link", "ganon"}; // Works
}
public String[] getNames() {
  return {"zelda", "link", "ganon"}; // Doesn't work
}

dg stream:
int[] intArray = IntStream.range(1, 11).toArray();
int[] intArray = IntStream.rangeClosed(1, 10).toArray();
int[] intArray = IntStream.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).toArray();

int[] intArray = new int[]{6, 2, 4, 5, 7};
int[] intArray = IntStream.of(6, 2, 4, 5, 7).toArray();
[6, 2, 4, 5, 7]

int[] intArray = IntStream.of(6, 2, 4, 5, 7).sorted().toArray();
[2, 4, 5, 6, 7]

Array<String> myarr = ArrayList<String>()
kotlin:
val nums = arrayOf(1, 2, 3, 4, 5)
val nums = arrayOf(1, 2, 3, 4, 5, 6, 7)
val nums2 = (3..12).toList().toTypedArray()
val nums3 = IntArray(5, { i -> i * 2 + 3})
val nums = intArrayOf(1, 2, 3, 4, 5)

arrayOf, arrayListOf, IntArray, IntArrayOf...

mengenal kotlin range
https://youtu.be/VtEU1FP5MEc?t=1840
val rng = 1..10
val rng = 1 until 10 (1..9)
val rng = 'A'..'Z'
val rng = 10.downTo(1)
val rng = 2.rangeTo(20)
val rng = (1..10).step(3) // 1 (starting point), 4, 7, 10

rng.reversed()

oh ya utk javascript kita belum masukk Array(s).from ...

mengenal IntStream java
java.util.stream.IntStream
java.util.stream.Stream

is.of(...list of ints...)
is.range().reduce()
is.of(1,2,3,4,5).forEach(..) -> System.out::println
is.range(1,6).forEach(..)
is.rangeClosed(1,5).forEach(..)
is.iterate(0, i->i+2).forEach(..)

java.util.concurrent.ThreadLocalRandom
is.generate(
  ()->ThreadLocalRandom.current().nextInt()
)
.limit(5)
.forEach(..)
is
.rangeClosed(1,5)
.map(i->i*i)
.forEach(..)

is
.rangeClosed(1,5)
.filter(i->i%2==0)
.forEach(..)

is
.rangeClosed(1,5)
.mapToObj(i->" "+i) // jadi Stream<String>
.forEach(..)

Stream<Integer> si = is
.rangeClosed(1,5)
.boxed() // jadi Stream<Integer>

mengenai Array.from di javascript

?An

di sini ada
buat array saja (secara nama)
alokasi memori sebanyak 10
inisialisasi dg 10 items
