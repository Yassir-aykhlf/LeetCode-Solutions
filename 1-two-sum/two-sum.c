#define TABLE_SIZE 10

typedef struct s_node
{
    int             number;
    int             pos;
    struct  s_node *next;
} t_node;

typedef struct s_table
{
    t_node  *bucket[TABLE_SIZE];
}   t_table;

unsigned int hash(int number)
{
    return (unsigned int)(abs(number) % TABLE_SIZE);
}

void    insert(t_table *table, int number, int pos)
{
    unsigned int    index = hash(number);
    t_node          *node = malloc(sizeof(t_node));

    node->number = number;
    node->pos = pos;
    node->next = table->bucket[index];
    table->bucket[index] = node;
}

t_table    *create_table(void)
{
    t_table *table = malloc(sizeof(t_table));
    if (!table)
        return NULL;
    for (int i = 0; i < TABLE_SIZE; i++) {
        table->bucket[i] = NULL;
    }
    return table;
}

int search(t_table *table, int remainder)
{
    unsigned int remainder_pos = hash(remainder);
    t_node  *current = table->bucket[remainder_pos];

    while (current)
    {
        if (current->number == remainder)
            return (current->pos);
        current = current->next;
    }
    return (-1);
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    t_table *table = create_table();
    int     *output = malloc(2 * sizeof(int));
    int     remainder;
    int     pos;

    for (int i = 0; i < numsSize; i++)
        insert(table, nums[i], i);
    for (int i = 0; i < numsSize; i++) {
        remainder = target - nums[i];
        pos = search(table, remainder);
        if (pos > i)
        {
            output[0] = i;
            output[1] = pos;
            *returnSize = 2;
            return output;
        }
    }
    free(output);
    return NULL;
}