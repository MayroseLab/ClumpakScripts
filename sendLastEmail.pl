use strict;
use warnings;

use Getopt::Long;

my $toEmail;
my $id;
my $subjectEmail = "";

GetOptions(
	"toEmail=s"        => \$toEmail,
	"id=s"     => \$id, 
	"subject=s"     => \$subjectEmail
);

my $from = 'evolseq@tauex.tau.ac.il';

my $subject;

if ($subjectEmail ne "") {
	$subject = $subjectEmail;
}
else {
	$subject = 'CLUMPAK results';
}

my $resultsLink = 'http://clumpak.tau.ac.il/results.html?jobId=';
$resultsLink = $resultsLink."$id";

my $message = 'Thanks you for using CLUMPAK. View your job\'s results here:';
$message = $message."$resultsLink";
 
open(MAIL, "|/usr/sbin/sendmail -t");
 
# Email Header
print MAIL "To: $toEmail\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n\n";

# Email Body
print MAIL $message;

close(MAIL);
print "Email Sent Successfully to: $toEmail\n";

