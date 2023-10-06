/* Implement Trie (Prefix Tree)
*  
*  A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
*  
*  Implement the Trie datastructure:
*  
*  trueCreate() Initializes the trie struct.
*  void insert(String word) Inserts the string word into the trie.
*  boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
*  boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
*  
*/

#define ALPHABET_SIZE 26

typedef struct trie
{
    bool terminal;
    struct Trie *children[ALPHABET_SIZE];
} Trie;

Trie *trieCreate()
{
    Trie *trie = malloc(sizeof(Trie));
    assert(trie != NULL);
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        trie->children[i] = NULL;
    }
    trie->terminal = false;
    return trie;
}

void trieInsert(Trie *obj, char *word)
{
    Trie *current = obj;
    while (*word)
    {
        char idx = (*word) - 'a';
        /* Letter is not present, insert a ref to new trie at letter index */
        if (current->children[idx] == NULL)
        {
            current->children[idx] = trieCreate();
        }
        current = current->children[idx];
        word++;
    }
    current->terminal = true;
}

bool trieSearch(Trie *obj, char *word)
{
    Trie *current = obj;
    while (*word)
    {
        char idx = (*word) - 'a';
        if (current->children[idx] == NULL)
        {
            return false;
        }

        current = current->children[idx];
        word++;
    }
    return current->terminal;
}

bool trieStartsWith(Trie *obj, char *prefix)
{
    Trie *current = obj;
    while (*prefix)
    {
        char idx = (*prefix) - 'a';
        if (current->children[idx] == NULL)
        {
            return false;
        }
        current = current->children[idx];
        prefix++;
    }
    return true;
}

void trieFree(Trie *obj)
{
    Trie *current = obj;
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if (current->children[i])
        {
            trieFree(current->children[i]);
            free(current->children[i]);
        }
    }
}
