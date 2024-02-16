#include "lists.h"
/**
 * is_palindrome - check if the list is_palindrome
 * @head: the head of the linked list
 * Return: true if palindrome exist
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = (*head);
	listint_t *fast = (*head);
	listint_t *splited_list = NULL;
	listint_t *temp, *temp1;

	if (*head == NULL)
		return (false);
	/*spilt the list*/
	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	splited_list = slow->next;
	slow->next = NULL;

	temp = reverse(&splited_list);
	temp1 = *head;
	while (temp && temp1)
	{
		if (temp->n != temp1->n)
			return (false);
		temp = temp->next;
		temp1 = temp1->next;
	}
	return (true);
}
/**
 * reverse - reverse a linked list
 * @head: the head of the linked list
 * Return: the reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *link = NULL;

	while (*head)
	{
		link = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = link;
	}
	*head = prev;
	return (*head);
}
