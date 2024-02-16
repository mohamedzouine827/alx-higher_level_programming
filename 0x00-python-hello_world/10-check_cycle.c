#include "lists.h"
/**
 * check_cycle - check if there's a cycle
 * @list: list
 * Return: 0 if not , 1 if
 */
int check_cycle(listint_t *list)
{
	listint_t *bati2 = list;
	listint_t *sari3 = list;

	if (!list || !list->next)
	{
		return (0);
	}
	bati2 = list->next;
	sari3 = list->next->next;

	while (bati2 && sari3 && sari3->next)
	{
		if (bati2 == sari3)
		{
			return (1);
		}
		bati2 = bati2->next;
		sari3 = sari3->next->next;
	}
	return (0);
}
