Changelog
---------

Unreleased
~~~~~~~~~~

1.2.3 (2016-01-07)
~~~~~~~~~~~~~~~~~~~

- Fixes daily e-mail sometimes being sent twice.
  [href]

1.2.2 (2016-01-05)
~~~~~~~~~~~~~~~~~~~

- Fixes cronjobs not working with more than one process.
  [href]

1.2.1 (2016-01-04)
~~~~~~~~~~~~~~~~~~~

- Fixes news link on homepage.
  [href]

1.2.0 (2016-01-04)
~~~~~~~~~~~~~~~~~~~

- Adds a status mail sent to all users daily at 08:30.
  [href]

- Adds a user profile where users can change their settings.
  [href]

- Shows the contact address in emails in a single line.
  [href]

- Greys out the 'reserve' link for unavailable allocations.
  [href]

- Adds the ability to add extra notes to people.
  [href]

1.1.0 (2015-12-30)
~~~~~~~~~~~~~~~~~~~

- Fixes being unable to save a page after a linked person has been deleted.
  [href]

- Adds an "all news" link to the homepage and removes the 'more...' links.
  [href]

- Adds the ability to filter the news page by year. In addition each available
  year is linked on the frontpage.
  [href]

- Adds a custom 404 page.
  [href]

- Improves printing styles, especially the printing of tickets.
  [href]

- Ensures that page links are always rendered right after the text.
  [href]

- Only updates the builtin forms if there have been any changes. This leads
  to faster startup time and improves the page rendering time if elasticsearch
  is offline when the process is restarted.
  [href]

- Improves ticket confirmation text.
  [href]

- Improves the event publication terms and conditions text.
  [href]

1.0.2 (2015-12-21)
~~~~~~~~~~~~~~~~~~~

- Depends on latest onegov.core which fixes an issue with date display.
  [href]

- Is more consistent with the use of secondary buttons in input fields.
  [href]

1.0.1 (2015-12-17)
~~~~~~~~~~~~~~~~~~~

- Shows a helpful error if a form with an existing name is added.
  [href]

- Enables picture upload on person edit view.
  [href]

- Fixes datetime picker not working in the events view.
  [href]

1.0.0 (2015-12-17)
~~~~~~~~~~~~~~~~~~~

- Localize date input format.
  [msom]

- Opens links pointing to files in a new tab.
  [href]

- Improves ticket state change error handling.
  [href]

- Replaces the town name with the contact info in the email footer.
  [href]

- Improves datetime picker on Firefox/Safari/Internet Explorer.
  [href]

0.11.2 (2015-12-08)
~~~~~~~~~~~~~~~~~~~

- Displays a helpful error when the daypass quota is invalid.
  [href]

- Ensures a difference between the pending and the open tickets color.
  [href]

0.11.1 (2015-12-07)
~~~~~~~~~~~~~~~~~~~

- Properly uses singular/plural for ticket display.
  [href]

- Improves the display of the footer.
  [href]

0.11.0 (2015-12-04)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to select images, files and internal links throug dialogs.
  [href]

- Adds terms to events submission form.
  [msom]

- Improves the display of open/pending tickets for logged in users.
  [href]

- Fixes invalid start/end times in allocations leading to an exception.
  [href]

- Stops person/page move from leading to an exception in certain cases.
  [href]

- Displays the function of a person in the overview.
  [href]

0.10.1 (2015-11-30)
~~~~~~~~~~~~~~~~~~~

- Adds people re-ordering for forms and resources in addition to pages.
  [href]

- Improvres readability of fullcalendar.
  [href]

0.10.0 (2015-11-27)
~~~~~~~~~~~~~~~~~~~

- Adds an extra confirmation step to the reservations to be more consistent
  with the way form and event submissions work.
  [href]

- Adds the ability to reserve parts of an allocation. Allocations in rooms are
  partly reservable by default.
  [href]

- Adds the ability to re-order people in the people's panel. Works just like
  page reorderings do.
  [href]

- Don't show a grey box below images with an empty alt text.
  [href]

- Removes extra spaces occurring on certain contact panels.
  [href]

- Fixes umlauts in the search box leading to decoding errors.
  [href]

0.9.2 (2015-11-24)
~~~~~~~~~~~~~~~~~~~

- Fixes display issue in the calendar.
  [href]

0.9.1 (2015-11-24)
~~~~~~~~~~~~~~~~~~~

- Hides 'no lead-in' hint on news overview.
  [href]

- Renders image captions a bit more subtle.
  [href]

- Improves the legibility of small allocations in the calendar.
  [href]

- Improves display of new reservation form.
  [href]

0.9.0 (2015-11-20)
~~~~~~~~~~~~~~~~~~~

- Hides hidden resources in the overview.
  [href]

- Shows missing lead info on resources and forms in addition to pages.
  [href]

- The user is no longer logged-in right after a password reset.

  This increases security by making sure that this is not a backdoor to
  circumvent future 2FA implementations.
  [href]

- Removes the double scrollbars in the file select dialog.
  [href]

- Improves file/image upload styling, adding a progress bar for uploads.
  [href]

0.8.1 (2015-11-18)
~~~~~~~~~~~~~~~~~~~

- Fixes a critical issue which could result in lost reservations.
  [href]

0.8.0 (2015-11-18)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to override the default labels for the online counter,
  the reservations and the sbb daypass on the homepage.
  [href]

- Improves print styles.
  [msom]

- Adds image captions.
  [msom]

- Improves event list for mobiles.
  [msom]

- Adds ticket reference to event mails.
  [msom]

- Hides "open in new tab" and "text orientation" in image edit dialog.
  [msom]

- Fixes generation of faulty empty tags in mark_images.
  [msom]

- Sorts uploaded files alphabetically.
  [msom]

- Adds social media links.
  [msom]

- Adds links to contact page and opening hours page.
  [msom]

- Visualizes the contrast ratio of the primary color with a meter.
  [msom]

- Shows a warning if a page contains no lead.
  [msom]

0.7.1 (2015-10-26)
~~~~~~~~~~~~~~~~~~~

- Makes sure the page move api only accepts numbers for its ids.
  [href]

- Introduces a delay to drag & drop operations to prevent accidents.
  [href]

0.7.0 (2015-10-22)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to have topics and links appear on the frontpage by
  selecting a checkbox on the edit dialog.
  [href]

- Adds the ability to order pages using drag & drop in the sidebar.
  [href]

- People are now always rendered "Firstname Lastname", without salutation.
  [href]

0.6.6 (2015-10-19)
~~~~~~~~~~~~~~~~~~~

- Change default locale from 'de_ch' to 'de_CH', as the former does not exist.
  [href]

0.6.5 (2015-10-16)
~~~~~~~~~~~~~~~~~~~

- Updates redactor to 10.2.5.
  [href]

- Switch from 'de' to 'de_CH' to properly support Swiss formatting.
  [href]

- Removes Python 2.x support.
  [href]

- Logouts now redirect to the current page, just like logins.
  [href]

- Fixes various little design issues.
  [href]

- Fixes elasticsearch offline warning being recorded mistakenly.
  [href]

0.6.4 (2015-09-29)
~~~~~~~~~~~~~~~~~~~

- Fixes search being unable to find certain people.
  [href]

0.6.3 (2015-09-29)
~~~~~~~~~~~~~~~~~~~

- Adds catalog A-Z.
  [href]

0.6.2 (2015-09-29)
~~~~~~~~~~~~~~~~~~~

- Fixes small design issues on mobile.
  [href]

0.6.1 (2015-09-28)
~~~~~~~~~~~~~~~~~~~

- Limits the height of the people's list in the edit dialog.
  [href]

- Updates redactor to 10.2.4.
  [href]

0.6.0 (2015-09-25)
~~~~~~~~~~~~~~~~~~~

- Adds a fulltext search feature with fast results and autocomplete.
  [href]

- Adds URLs to ical exports.
  [msom]

0.5.1 (2015-09-10)
~~~~~~~~~~~~~~~~~~~

- Improves the error handling in form definitions.
  [href]

- The people's portraits are now always covering their surrounding block.
  [href]

- Fixes page link ordering below page content.
  [href]

- Adds ical exports to events.
  [msom]

- Disables delete event link if a ticket exists.
  [msom]

0.5.0 (2015-09-04)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to enter, list and manage events (parties, concerts, etc.).
  [msom]

- Adds a function field to the person.
  [href]

- Adds the ability to clean up unused allocations.
  [href]

- Updates redactor to 10.2.3.
  [href]

- Adds the ability to filter tickets by handler.
  [href]

- Adds the ability to show all tickets of all states in one table.
  [href]

- Adds a link between allocation and tickets.
  [href]

- Sorts the children pages on the homepage by A-Z as well.
  [href]

- Includes the submitter e-mail address on the ticket view.
  [href]

0.4.0 (2015-08-28)
~~~~~~~~~~~~~~~~~~~

- The allocation availability calculation is now faster and accurate.
  [href]

- Expired reservation sessions are now automatically removed.
  [href]

- Adds the ability to create reservations and to accept/reject them.
  [href]

- The edit links for the model shown on the ticket view are now only visible
  if the ticket is in 'pending' state. To change something on the model, the
  ticket needs to be accepted/reopened.
  [href]

- All forms now retain the posted value if a validation error occurs.
  [href]

- Adds the ability to define the reservation form on the resource.
  [href]

0.3.10 (2015-08-25)
~~~~~~~~~~~~~~~~~~~

- Replaces the broken 'jsmin' filter with the not so broken 'rjsmin' filter.
  [href]

- Depends on latest onegov.core - with this release the upgrade tables should
  be set up correctly when creating new schemas.
  [href]

0.3.9 (2015-08-20)
~~~~~~~~~~~~~~~~~~~

- Reservation allocations can now be created/modified and deleted.
  [href]

- Adds the ability to confirm the confirmation dialog using enter. To cancel
  press escape.
  [href]

- A person's academic title is now a person's salutation.
  [href]

- Removes Gravatar support.
  [href]

0.3.8 (2015-08-14)
~~~~~~~~~~~~~~~~~~~

- Emails are now sent only if the db transaction is successful.
  [href]

0.3.7 (2015-08-12)
~~~~~~~~~~~~~~~~~~~

- Fixes some email sending issues.
  [href]

0.3.6 (2015-08-12)
~~~~~~~~~~~~~~~~~~~

- Makes sure that all person links are valid.
  [href]

- When inserting a defined link, the dropdown now starts with an empty selection.
  [href]

0.3.5 (2015-08-11)
~~~~~~~~~~~~~~~~~~~

- Fix code editor not working in form definition editor.
  [href]

0.3.4 (2015-08-11)
~~~~~~~~~~~~~~~~~~~

- Depends on latest onegov.form release to fix installation issue.
  [href]

- The onegov.town.element classes now use less memory.
  [href]

0.3.3 (2015-08-10)
~~~~~~~~~~~~~~~~~~~

- Improves upon the requirements.txt generation. No other changes.
  [href]

0.3.2 (2015-08-10)
~~~~~~~~~~~~~~~~~~~

- No changes worth mentioning. Experimental requirements.txt generation on release.
  [href]

0.3.1 (2015-08-07)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to insert site links in the redactor through a dropdown.
  [href]

- Limit the deletion of pages including subpages to users with the admin role.
  [href]

- Adds a copy&paste mechanism for pages, links and news.
  [href]

- Add the ability to define room/daypass resources and allocations (no way
  to do reservations just yet).
  [href]

- Group images by dates.
  [msom]

0.3.0 (2015-08-03)
~~~~~~~~~~~~~~~~~~~

- Correctly sort the the pages even if the title has changed.
  [href]

- Limits the news list on the homepage to two entries.
  [href]

- Adds the datetimepicker plugin.
  [msom]

- Add retrieve password functionality.
  [msom]

0.2.6 (2015-07-16)
~~~~~~~~~~~~~~~~~~~

- Fixes encoding issue in Apple Mail.
  [href]

0.2.5 (2015-07-16)
~~~~~~~~~~~~~~~~~~~

- Shows a ticket count at the top of every page for logged in users.
  [href]

- Adds e-mail notifications for open/close ticket.
  [href]

- Adds reopen ticket functionality.
  [msom]

- Adds analytics code snippet.
  [msom]

0.2.4 (2015-07-14)
~~~~~~~~~~~~~~~~~~~

- Integrates tickets through onegov.ticket.
  [href]

- Form submissions automatically generate a onegov.ticket in the backend.
  [href]

- The old form submissions colleciton view is no more. This is now done
  through the ticketing system.
  [href]

- Form submissions, tickets and news are now shown with a relative date
  (e.g. 5 hours ago).
  [href]

0.2.3 (2015-07-09)
~~~~~~~~~~~~~~~~~~~

- Each form must now contain at least one required e-mail address field.
  [href]

- The login link always redirects to the original site now.
  [href]

- Show an alert for every form that contains errors.
  [href]

- Adds a reply-to address for automated e-mails.
  [href]

- Show the edit/delete links outside the dropdown.
  [href]

- Adds the ability to add an address block to topics, news and forms.
  [href]

- Adds the ability to add people to topics, news and forms.
  [href]

0.2.2 (2015-07-03)
~~~~~~~~~~~~~~~~~~~

- Show sidebar below the content on smaller screens.
  [href]

- Adds the ability to keep a directory of people related to the town.
  [href]

- Fix lists not showing a dot in the redactor editor.
  [href]

- Adds files upload and listing.
  [treinhard]

- Use more pronounced colors for various elements.
  [href]

- Adds the ability to hide news, pages or forms from anonymous users.
  [href]

- Fix sticky footer being partly rendered out of the viewport.
  [href]

- Updates Redactor to 10.2.
  [href]

0.2.1 (2015-06-26)
~~~~~~~~~~~~~~~~~~~

- Adds support for onegov.core.upgrade.
  [href]

- Remove support for Python 3.3.
  [href]

- Pages are now always sorted from A to Z.
  [href]

- Fixes form dependency javascript not working with multiple choices.
  [href]

- Fixes greyscale scss mixin not working in Firefox.
  [href]

- Adds many new builtin forms.
  [freinhard]

- Adds minor style adjustments.
  [freinhard]

0.2.0 (2015-06-10)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to use builtin forms, define custom forms and manage
  submissions.

- The 'more...' news link is only showed if there actually is more to read.
  [href]

- Paragraphs are now limited in width, images are 100% width.
  [href]

- Fix sticky footer jumping in Chrome by fixating it using CSS.
  [href]

0.1.0 (2015-05-07)
~~~~~~~~~~~~~~~~~~~

- Adds a news section.
  [href]

- Refactors pages to be easily be able to define new kind of pages.
  [href]

- Adds contact and opening hours as a footer.
  [href]

0.0.2 (2015-05-05)
~~~~~~~~~~~~~~~~~~~

- Images are now always shown in order of their creation.
  [href]

- Adds image thumbnails and the ability to select previously uploaded images
  in the html editor.
  [href]

- Adds support for image uploads through the html editor.
  [href]

- Replaces the markdown editor with a WYSIWYG html editor.
  [href]

- Upgrade to Zurb Foundation 5.5.2.
  [href]

- Show a wildcard next to required form fields.
  [href]

- Adds hints to form fields, rendered as placemarks.
  [href]

- The page markdown editor no longer steals the focus when opening the page.
  [href]

0.0.1 (2015-04-29)
~~~~~~~~~~~~~~~~~~~

- Initial release.
  [href]
