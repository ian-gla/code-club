## Introduction

This is has been adapted from a [code-wars problem](https://www.codewars.com/kata/592bdf59912f2209710000e9).

The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which act as a simple replacement cypher.

The most frequently used key is "GA-DE-RY-PO-LU-KI".
```
 g => a
 a => g
 d => e
 e => d
  etc.
```
The letters which are not on the list of substitutes stay in the encrypted text without changes.

Other keys often used by Scouts:
```
PO-LI-TY-KA-RE-NU
KA-CE-MI-NU-TO-WY
KO-NI-EC-MA-TU-RY
ZA-RE-WY-BU-HO-KI
BA-WO-LE-TY-KI-JU
RE-GU-LA-MI-NO-WY
```
## Task

Our scouts had party yesterday and they had too much milk and cookies. As a result all of them forgot the key. Your task is to help the scouts find the key they used for encryption by writing a `find_the_key()` function. Fortunately they have some messages that are already encoded.

The function `find_the_key()` should accept two lists as parameters: `messages` and `secrets`.
The strings on the `messages` list are the scout's messages before encryption, consisting of strings of lowercase characters and whitespace characters.
The strings on the `secrets` list are the scout's messages after encryption, also consisting of strings of lowercase characters and whitespace characters. 

The function should return a string consisting of lowercase characters only. The pairs of substitution should be ordered by the first letter of substitution. The letters in each pair should be in alphabetic order. For example:

```
ga => incorrect output (error: g is after a )
ag => correct output  
deag => incorrect output  (error: de is after ag)
agde => correct output  
```

## Example

```
messages = ["dance on the table", "hide my beers", "scouts rocks"]
secrets = ["egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" ]
find_the_key(messages, secretes)   //=> agdeikluopry
```
