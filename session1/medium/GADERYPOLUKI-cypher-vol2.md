## Introduction
This has been adapted from a [Code-Wars problem](https://www.codewars.com/kata/592b7b16281da94068000107).

The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which act as a simple replacement cypher.

The most frequently used key is "GA-DE-RY-PO-LU-KI".
```
 G => A
 g => a
 a => g
 A => G
 D => E
  etc.
```

The letters which are not on the list of substitutes stay in the encrypted text without changes.

Other keys often used by Scouts are:
```
PO-LI-TY-KA-RE-NU
KA-CE-MI-NU-TO-WY
KO-NI-EC-MA-TU-RY
ZA-RE-WY-BU-HO-KI
BA-WO-LE-TY-KI-JU
RE-GU-LA-MI-NO-WY
```

## Task

Your task is to help scouts to encrypt and decrypt thier messages by writing `encode()` and `decode()` functions.

The functions should have two parameters, `message` and `key`.
The `message` input string consists of lowercase and uperrcase characters and whitespace characters.
The `key` input string consists of only lowercase characters.
The substitution should be case-sensitive.

## Example
```
 encode("ABCD", "agedyropulik");             // => GBCE 
 encode("Ava has a cat", "gaderypoluki");    // => Gvg hgs g cgt 
 decode("Dkucr pu yhr ykbir","politykarenu") // => Dance on the table
 decode("Hmdr nge brres","regulaminowy")     // => Hide our beers
```
