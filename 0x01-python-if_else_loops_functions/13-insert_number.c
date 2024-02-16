#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = *head, *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	if (new_node == NULL || new_node->n >= number)
	{
		node->next = new_node;
		*head = node;
		return (node);
	}
	while (new_node && new_node->next && new_node->next->n < number)
		new_node = new_node->next;
	node->next = new_node->next;
	new_node->next = node;
	return (node);
}
