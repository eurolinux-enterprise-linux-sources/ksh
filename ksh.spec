%define       releasedate   2012-08-01

Name:         ksh
Summary:      The Original ATT Korn Shell
URL:          http://www.kornshell.com/
Group:        System Environment/Shells
#zlib is used for INIT.2010-02-02.tgz/src/cmd/INIT/ratz.c - used only for build tool
#EPL everywhere else (for KSH itself)
License:      EPL
Version:      20120801
Release:      35%{?dist}
Source0:      http://www.research.att.com/~gsf/download/tgz/ast-ksh.%{releasedate}.tgz
Source1:      http://www.research.att.com/~gsf/download/tgz/INIT.%{releasedate}.tgz
Source3:      kshrc.rhs
Source4:      dotkshrc

# documentation of important changes not mentioned in RELEASE file
Source5:      ChangeLog

# expected results of test suite
%global testresults  %{_sourcedir}/expectedresults.log

# don't use not wanted/needed builtins - Fedora/RHEL specific
Patch1:       ksh-20070328-builtins.patch

# fix regression test suite to be usable during packagebuild - Fedora/RHEL specific
Patch2:      ksh-20100826-fixregr.patch

# fedora/rhel specific, rhbz#619692
Patch6:       ksh-20080202-manfix.patch

# rhbz#702008
Patch17:      ksh-20100202-pathvar.patch

# rhbz#924440
Patch18:      ksh-20100621-fdstatus.patch

# fixes for regressions found in ksh-20120801 rebase
Patch19:      ksh-20120801-rmdirfix.patch
Patch20:      ksh-20120801-cdfix.patch
Patch21:      ksh-20120801-cdfix2.patch
Patch22:      ksh-20120801-tabfix.patch
Patch23:      ksh-20130214-fixkill.patch

# for ksh <= 2013-05-31, rhbz#960034
Patch24:      ksh-20120801-kshmfix.patch

# for ksh <= 2016-06-28, rhbz#921455
Patch25:      ksh-20120801-memlik.patch

# for ksh <= 2013-03-20, rhbz#922851
Patch26:      ksh-20120801-forkbomb.patch

# for ksh <= 2013-04-19, rhbz#913110, rhbz#994251
Patch27:      ksh-20120801-macro.patch

# revert change in behaviour so rebased package behaves still the same
Patch28:      ksh-20120801-revert001.patch

# not completely upstream yet, rhbz#858263
Patch29:      ksh-20130628-longer.patch

# for ksh <= 2013-07-19, rhbz#982142
Patch30: ksh-20120801-mlikfiks.patch

# not yet upstream, related to 2012-08-01 rebase
Patch31: ksh-20120801-covsfix.patch

# rhbz#1007816
Patch32: ksh-20100621-manfix3.patch

# rhbz#1016611
Patch33: ksh-20120801-nomulti.patch

# from upstream, rhbz#1036802
Patch34: ksh-20120801-fd2lost.patch

# for ksh <= 2014-01-14, rhbz#1036470
Patch35: ksh-20120801-memlik3.patch

# for ksh <= 2014-03-04, rhbz#1066589
Patch36: ksh-20120801-filecomsubst.patch

# for ksh <= 2014-04-05, rhbz#825520
Patch37: ksh-20120801-crash.patch

# for ksh < 2013-03-19, rhbz#1075635
Patch38: ksh-20120801-sufix.patch

# for ksh < 2014-03, rhbz#1047506
Patch39: ksh-20120801-argvfix.patch

# sent upstream, rhbz#1078698
Patch40: ksh-20140301-fikspand.patch

# for ksh < 2014-04-15, rhbz#1070350
Patch41: ksh-20120801-roundit.patch

# for ksh < 2014-04-15, rhbz#1036931
Patch42: ksh-20120801-heresub.patch

# not included upstream yet, rhbz#1062296
Patch43: ksh-20140415-hokaido.patch

# for ksh < 20121004, rhbz#1083713
Patch44: ksh-20120801-tpstl.patch

# for ksh <= 20120214, rhbz#1023109
Patch45: ksh-20120801-mtty.patch

# sent upstream, rhbz#1019334
Patch46: ksh-20120801-manfix4.patch

# not upstream yet, rhbz#1105138
Patch47: ksh-20120801-fununset.patch

# not upstream yet, rhbz#1102627
Patch48: ksh-20120801-cdfix3.patch

# sent upstream, rhbz#1112306
Patch49: ksh-20120801-locking.patch

# for ksh <= 2013-06-13, rhbz#1133582
Patch50: ksh-20130613-cdfix4.patch
Patch51: ksh-20120801-retfix.patch

# not upstream yet, rhbz#1147645
Patch52: ksh-20120801-oldenvinit.patch

# not upstream yet, rhbz#1160923
Patch53: ksh-20120801-noexeccdfix.patch

# sent upstream, for ksh <= 2014-09-30, rhbz#1168611
Patch54: ksh-20120801-cdfork.patch

# from upsteam, for ksh < 2012-10-04, rhbz#1173668
Patch55: ksh-20120801-emptyarrayinit.patch

# not upstream yet, rhbz#1188377
Patch56: ksh-20120801-xufix.patch

# sent upstream, for ksh <= 2015-02-10, rhbz#1189294
Patch57: ksh-20120801-assoc-unset-leak.patch

# sent upstream, for ksh <= 2014-12-18, rhbz#1176670
Patch58: ksh-20120801-alarmifs.patch

# not yet upstream, rhbz#1116072
Patch59: ksh-20140929-safefd.patch

# workaround, for ksh < 2013-05-24, rhbz#1117404
Patch60: ksh-20120801-trapcom.patch

# not upstream yet, for ksh <= 2015-04-03, rhbz#1200534
Patch61: ksh-20140801-arraylen.patch

Patch62: ksh-20120801-badgcc.patch

# sent upstream, for ksh <= 2015-08-24, rhbz#1256495
Patch63: ksh-20120801-mb-after-argvar.patch

# not yet upstream, rhbz#1217236
Patch64: ksh-20120801-nohupfork.patch

# from upstream, for ksh <= 20130409, rhbz#1241013
Patch65: ksh-20120801-parserfix.patch

# sent upstream, for ksh <= 2014-09-29, rhbz#1212992
Patch66: ksh-20140801-diskfull.patch

# Sent upstream, rhbz#1324990
Patch67: ksh-20120801-subshell-leak.patch

# rhbz#1437530
Patch68: ksh-20120801-dotdoublefree.patch

BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Conflicts:    pdksh
Requires: coreutils, diffutils, chkconfig
BuildRequires: bison
Requires(post): grep, coreutils, chkconfig
Requires(preun): grep, coreutils, chkconfig

%description
KSH-93 is the most recent version of the KornShell by David Korn of
AT&T Bell Laboratories.
KornShell is a shell programming language, which is upward compatible
with "sh" (the Bourne Shell).

%prep
%setup -q -c
%setup -q -T -D -a 1
%patch1 -p1 -b .builtins
%patch2 -p1 -b .fixregr
%patch6 -p1 -b .manfix
%patch17 -p1 -b .pathvar
%patch18 -p1 -b .fdstatus
%patch19 -p1 -b .rmdirfix
%patch20 -p1 -b .cdfix
%patch21 -p1 -b .cdfix2
%patch22 -p1 -b .tabfix
%patch23 -p1 -b .fixkill
%patch24 -p1 -b .kshmfix
%patch25 -p1 -b .memlik
%patch26 -p1 -b .forkbomb
%patch27 -p1 -b .macro
%patch28 -p1 -b .revert001
%patch29 -p1 -b .longer
%patch30 -p1 -b .mlikfiks
%patch31 -p1 -b .covsfix
%patch32 -p1 -b .manfix3
%patch33 -p1 -b .nomulti
%patch34 -p1 -b .fd2lost
%patch35 -p1 -b .memlik3
%patch36 -p1 -b .filecomsubst
%patch37 -p1 -b .crash
%patch38 -p1 -b .sufix
%patch39 -p1 -b .argvfix
%patch40 -p1 -b .fikspand
%patch41 -p1 -b .roundit
%patch42 -p1 -b .heresub
%patch43 -p1 -b .hokaido
%patch44 -p1 -b .tpstl
%patch45 -p1 -b .mtty
%patch46 -p1 -b .manfix4
%patch47 -p1 -b .fununset
%patch48 -p1 -b .cdfix3
%patch49 -p1 -b .locking
%patch50 -p1 -b .cdfix4
%patch51 -p1 -b .retfix
%patch52 -p1 -b .oldenvinit
%patch53 -p1 -b .noexeccdfix
%patch54 -p1 -b .cdfork
%patch55 -p1 -b .emptyarrayinit
%patch56 -p1 -b .xufix
%patch57 -p1 -b .assoc-unset-leak
%patch58 -p1 -b .alarmifs
%patch59 -p1 -b .safefd
%patch60 -p1 -b .trapcom
%patch61 -p1 -b .arraylen
%patch62 -p1 -b .badgcc
%patch63 -p1 -b .mb-after-argvar
%patch64 -p1 -b .nohupfork
%patch65 -p1 -b .parserfix
%patch66 -p1 -b .diskfull
%patch67 -p1 -b .subshell-leak
%patch68 -p1 -b .dotdoublefree

cp %{SOURCE5} .

#/dev/fd test does not work because of mock
sed -i 's|ls /dev/fd|ls /proc/self/fd|' src/cmd/ksh93/features/options

# sh/main.c was not using CCFLAGS
sed -i '/-c sh\/main.c/s|${mam_cc_FLAGS} |${mam_cc_FLAGS} ${CCFLAGS} |p' src/cmd/ksh93/Mamfile

# disable register for debugging
sed -i 1i"#define register" src/lib/libast/include/ast.h

%build
XTRAFLAGS=""
for f in -Wno-unknown-pragmas -Wno-missing-braces -Wno-unused-result -Wno-return-type -Wno-int-to-pointer-cast -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable -Wno-cpp -P
do
  gcc $f -E - </dev/null >/dev/null 2>&1 && XTRAFLAGS="$XTRAFLAGS $f"
done
./bin/package
./bin/package make mamake ||:
./bin/package make mamake ||:
export CCFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing $XTRAFLAGS -DSHOPT_AUDIT"
export CC=gcc
./bin/package make -S

#missing in 2010-06-21, chech later if added back
#cp lib/package/LICENSES/ast LICENSE

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{/bin,%{_mandir}/man1}
install -c -m 755 arch/*/bin/ksh $RPM_BUILD_ROOT/bin/ksh93
install -c -m 644 arch/*/man/man1/sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ksh93.1
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.kshrc
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/kshrc

#fool rpmbuild about %ghost files
touch $RPM_BUILD_ROOT/bin/ksh
touch $RPM_BUILD_ROOT%{_mandir}/man1/ksh.1.gz

%check
[ -f ./skipcheck -o -f ./../skipcheck ] && exit 0 ||:
export SHELL=$(ls $(pwd)/arch/*/bin/ksh)
cd src/cmd/ksh93/tests/
ulimit -c unlimited
if [ ! -e /dev/fd ]
then
  echo "ERROR: /dev/fd does not exist, regression tests skipped"
  exit 0
fi
$SHELL ./shtests 2>&1 | tee testresults.log
[ ! -f %{testresults} ] && exit 0
sed -e '/begins at/d' -e '/ 0 error/d' -e 's/at [^\[]*\[/\[/' testresults.log -e '/tests skipped/d' >filteredresults.log
if ! cmp filteredresults.log %{testresults} >/dev/null || ls core.*
then
  echo "Regression tests failed"
  diff -Naurp %{testresults} filteredresults.log ||:
fi

%post
if [ ! -f /etc/shells ]; then
        echo "/bin/ksh" > /etc/shells
else
        if ! grep -q '^/bin/ksh$' /etc/shells ; then
                echo "/bin/ksh" >> /etc/shells
        fi
fi

%{_sbindir}/alternatives --install /bin/ksh ksh \
                /bin/ksh93 50 \
        --slave %{_mandir}/man1/ksh.1.gz ksh-man \
                %{_mandir}/man1/ksh93.1.gz

#if not symlink we are updating ksh where there was no alternatives before
#so replace with symlink and set alternatives
if [ ! -L /bin/ksh ]; then
        %{_sbindir}/alternatives --auto ksh
        ln -sf /etc/alternatives/ksh /bin/ksh
        ln -sf /etc/alternatives/ksh-man %{_mandir}/man1/ksh.1.gz
fi


%preun
if [ $1 = 0 ]; then
        %{_sbindir}/alternatives --remove ksh /bin/ksh93
fi

%postun
if [ ! -f /bin/ksh ]; then
	sed -i '/^\/bin\/ksh$/ d' /etc/shells
fi

%verifyscript
echo -n "Looking for ksh in /etc/shells... "
if ! grep '^/bin/ksh$' /etc/shells > /dev/null; then
    echo "missing"
    echo "ksh missing from /etc/shells" >&2
else
    echo "found"
fi

%files 
%defattr(-, root, root,-)
#%doc README LICENSE src/cmd/ksh93/COMPATIBILITY src/cmd/ksh93/RELEASE ChangeLog
%doc README src/cmd/ksh93/COMPATIBILITY src/cmd/ksh93/RELEASE ChangeLog
/bin/ksh93
%ghost /bin/ksh
%config(noreplace) %{_sysconfdir}/skel/.kshrc
%config(noreplace) %{_sysconfdir}/kshrc
%{_mandir}/man1/ksh93.1.gz
%ghost %{_mandir}/man1/ksh.1.gz

%clean
    rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jun 27 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-35
- Fix a crash during clean up after sourcing multiple files
  Resolves: #1437530

* Thu May 18 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-34
- Fix a memory leak while creating subshells
  Resolves: #1324990

* Fri Jan 08 2016 Michal Hlavinka <mhlavink@redhat.com> - 20120801-33
- ksh crashed when disk was full (#1212992)

* Thu Nov 26 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-32
- fix: in a login shell "( cmd & )" does nothing (#1217236)
- multibyte character string after $1-9 was not expanded correctly (#1256495)
- case in a for loop inside a subshell caused syntax error (#1241013)

* Wed Aug 19 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-31
- fix another occurence of previous bug (#1247383)

* Wed Aug 12 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-30
- do not free constant string trap (#1247383)

* Tue Jul 07 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-29
- prevent null-test optimization in strdup (#1221766)

* Fri Apr 03 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-28
- using trap DEBUG could cause segmentation fault (#1200534)

* Mon Mar 23 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-27
- ksh could hang when executed in removed directory (#1204111)

* Thu Mar 05 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-26
- fix segfault when handling a trap (#1117404)
- closing a file descriptor in a command substitution caused loss of the output (#1116072)

* Fri Feb 13 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-25
- combining alarm and IFS caused segfault (#1176670)

* Thu Feb 12 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-24
- cd to directory without execution permission can't fail silently (#1160923)
- current directory could differ from PWD (#1168611)
- declaration of a two dimemsional associatve array could add an extra 0 element (#1173668)
- exporting fixed with variable corrupted its data (#1188377)
- fixes memmory leak on unset of associative array (#1189294)

* Thu Feb 12 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-23
- do not inherit invalid variables during shell initializaton (#1147645)

* Thu Oct 02 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-22
- ksh hangs when command substitution containing pipe fills out the pipe buffer (#1138751)

* Tue Sep 02 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-21
- the last patch was not applied correctly (#1116508)

* Tue Sep 02 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-20
- return code from a function could be wrong (#1116508)

* Wed Aug 27 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-19
- cd builtin could break IO redirection (#1133582)

* Fri Jul 25 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-18
- job locking mechanism did not survive compiler optimization (#1112306)
- wrong return code from a pipe in command substitution (#1117316)

* Fri Jun 20 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-17
- do not crash when unsetting running function from another one (#1105138)
- should report an error when trying to cd into directory without execution bit (#1102627)

* Wed May 21 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-16
- do not resend signal on termination (#1075635)
- fix argv rewrite (#1047506)
- fix brace expansion on/off (#1078698)
- fix incorrect rounding of numsers 0.5 < |x| <1.0 in printf (#1070350)
- fix parser errors related to the end of the here-document marker (#1036931)
- ksh hangs when command substitution fills out the pipe buffer (#1062296)
- using typeset -l with a restricted variabled caused segmentation fault (#1083713)
- ksh stopped on read when monitor mode was enabled (#1023109)
- monitor mode was documented incorrectly (#1019334)

* Tue May 13 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-15
- fix segfault in job list code (#825520)

* Tue Mar 04 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-14
- reading a file via command substitution did not work when any of stdin,
  stdout or stderr were closed (#1066589)

* Wed Jan 22 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-13
- fix memory leak (#1036470)

* Mon Jan 20 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-12
- use different fix for last bug

* Fri Jan 10 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-11
- standard error output could get misdirected (#1036802)

* Wed Oct 16 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-10
- ksh sometimes wrote wrong byte sequence to terminal when vi editing 
  mode was used (#1016611) 

* Tue Sep 24 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-9
- ctrl-c during read did not kill job group (#960034)

* Fri Sep 13 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-8
- fix errors in man page (#1007816)

* Tue Aug 13 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-7
- fix command substitution in pipelines (#994241)

* Tue Jul 30 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-6
- fix license tag

* Mon Jul 29 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-5
- fix another memory leak (#982142)

* Mon Jul 22 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-4
- fix two memory leaks (#982142)

* Thu Jul 11 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-3
- assigment to right justified variables did not work correctly (#903750)

* Mon Jul 08 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-2
- fix overflow in subshell loop (#858263)
- set default editing mode to emacs (#761551)
- ksh -m did not turn monitor mode on (#960034)
- prevent fork bomb trigered by SIGSTP (#922851)

* Thu Jul 04 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-1
- updated to 20120801, fixes (#840568)
- fix several memory leaks (#921455) 

* Thu May 16 2013 Michal Hlavinka <mhlavink@redhat.com> - 20100621-22
- fix for command substitutions caused regressions, use different fix (#913110)

* Tue Apr 09 2013 Michal Hlavinka <mhlavink@redhat.com> - 20100621-21
- do not crash when using more file descriptors (#924440)

* Mon Mar 25 2013 Michal Hlavinka <mhlavink@redhat.com> - 20100621-20
- command substitution in here-document did not work propperly (#913110)

* Thu Nov 01 2012 Michal Hlavinka <mhlavink@redhat.com> - 20100621-19
- assigning a right justified typedef'd variable to a smaller one
  could corrupt the result (#846678)
- fix exporting of l/r-justified variable (#846678)

* Tue Oct 30 2012 Michal Hlavinka <mhlavink@redhat.com> - 20100621-18
- build with the logging ability (#869155)

* Tue Oct 02 2012 Michal Hlavinka <mhlavink@redhat.com> - 20100621-17
- flush output before forking (#827512)

* Wed Apr 11 2012 Michal Hlavinka <mhlavink@redhat.com> - 20100621-16
- tilda expansion does not work correctly (#800684)

* Wed Mar 07 2012 Michal Hlavinka <mhlavink@redhat.com> - 20100621-15
- do not crash when using a lot of file descriptors (#798868)

* Fri Mar 02 2012 Michal Hlavinka <mhlavink@redhat.com> - 20100621-14
- fix data corruption in a here-document section of a script at byte 8192 (#786787)
- restore tty settings after timed out read (#577223)
- do not create extra process when it's not needed (#781976)
- fix file descriptor leak (#781498)
- do not segfault on incorrect oop code (#743840)

* Mon Dec 19 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-13
- fix: ksh can exit prematurely without crash or any error (#742930)

* Tue Oct 11 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-12
- previous fix did not scale well, use different approach (#743842)

* Thu Oct 06 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-11
- ksh sometimes returns wrong exit code when pid numbers are being recycled (#743842)

* Tue Oct 04 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-10
- do not hang when pipes are used in eval argument (#742244)

* Wed Aug 10 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-9
- wait was returning incorrect value (#728900)
- last fix was incomplete, add missing part

* Fri Aug 05 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-8
- fix crash when IFS is unset inside a function - 2nd reproducer (#683734)

* Tue Jul 26 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-7
- ksh did not wait for pipeline to complete when pipefail option was used (#702016)
- completion used after an environment variable reported bad susbstituion error (#702015)
- ksh child exit code not preserved correctly (#702013)
- do not change $0 in posix function (#702011)
- fix man page information about default value for PATH variable (#702008)
- do not use invalid PID values in ksh kill built-in (#701890)
- fix crashe when IFS is unset inside a function (#683734)
- do not count empty array elements (#702014)

* Thu Mar 03 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-6
- fix ( ) compound list altering environment (#681478)

* Thu Feb 03 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-5
- fix for #616691 when combined with #616684 needs to be modified

* Mon Jan 17 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-4
- disable script aliasing optimization, because source code is not fully compliant

* Wed Jan 05 2011 Michal Hlavinka <mhlavink@redhat.com> - 20100621-3
- fix file io race condition when file was created, but still does not exist (#660319)
- use 'alternatives' for (m)ksh switching (#659658)
- do not forget to restore file handles after execution of sourced script (#651888)
- fix bug when here document got sometimes truncated (#644362)
- do not forget to close autoloaded file with function definition (#643811)
- fix wrong typeset handling of arrays that could caused a crash (#637052)
- fix minor issues in man page (#619692)
- fix crash when ksh get SIGPIPE while already executing signal handler (#616691)
- fix wrong output redirection in SIGPIPE trap (#616684)
- add RLIMIT_RTPRIO and RLIMIT_NICE support to ulimit (#582690)

* Tue Jun 29 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100621-2
- fix memory leak (second part is not upstream yet) (#586923)

* Tue Jun 29 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100621-1
- updated to 2010-06-21

* Mon May 31 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-9
- add pathmunge to /etc/kshrc

* Tue May 25 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-8
- fix rare cd builtin crash

* Tue May 04 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-7
- fix memory leak (#588710)

* Mon May 03 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-6
- fix infinite loop when whence builtin is used with -q option (#587127)
- fix stdin for double command substitution (#584704)

* Mon Mar 29 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-5
- fix typo in last patch

* Fri Mar 26 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-4
- restore tty settings after timed out read for utf-8 locale

* Fri Feb 19 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-3
- add zlib to license

* Wed Feb 10 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-2
- add COMPATIBILITY, RELEASE and ChangeLog to docs

* Tue Feb 09 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-1
- updated to stable version 2010-02-02

* Tue Jan 05 2010 Michal Hlavinka <mhlavink@redhat.com> - 20091224-1
- updated to 2009-12-24

* Mon Dec 07 2009 Michal Hlavinka <mhlavink@redhat.com> - 20091206-1
- updated to 2009-12-06

* Fri Dec 04 2009 Michal Hlavinka <mhlavink@redhat.com> - 20091130-1
- updated to 2009-11-30

* Wed Nov 18 2009 Michal Hlavinka <mhlavink@redhat.com> - 20091021-1
- updated to 2009-10-21

* Thu Aug 27 2009 Michal Hlavinka <mhlavink@redhat.com> - 20090630-1
- updated to 2009-06-30

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090505-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Michal Hlavinka <mhalvink@redhat.com> - 20090505-1
- updated to 2009-05-05

* Tue May 05 2009 Michal Hlavinka <mhalvink@redhat.com> - 20090501-1
- updated to 2009-05-01

* Tue Mar 10 2009 Michal Hlavinka <mhlavink@redhat.com> - 20081104-3
- fix typos in spec file

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Michal Hlavinka <mhlavink@redhat.com> 20081104-1
- update to 2008-11-04
- ast-ksh-locales are not useable remove them
- /usr/bin/ksh symlink was removed

* Tue Oct 21 2008 Michal Hlavinka <mhlavink@redhat.com> 20080725-4
- fix #467025 - Ksh fails to initialise environment when login from graphic console

* Wed Aug 06 2008 Tomas Smetana <tsmetana@redhat.com> 20080725-3
- fix BuildRequires, rebuild

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 20080725-2
- fix license tag

* Mon Jul 28 2008 Tomas Smetana <tsmetana@redhat.com> 20080725-1
- new upstream version

* Thu Jun 26 2008 Tomas Smetana <tsmetana@redhat.com> 20080624-1
- new upstream version

* Mon Feb 11 2008 Tomas Smetana <tsmetana@redhat.com> 20080202-1
- new upstream version

* Wed Jan 30 2008 Tomas Smetana <tsmetana@redhat.com> 20071105-3
- fix #430602 - ksh segfaults after unsetting OPTIND

* Mon Jan 07 2008 Tomas Smetana <tsmetana@redhat.com> 20071105-2
- fix #405381 - ksh will not handle $(xxx) when typeset -r IFS
- fix #386501 - bad group in spec file

* Wed Nov 07 2007 Tomas Smetana <tsmetana@redhat.com> 20071105-1
- new upstream version

* Wed Aug 22 2007 Tomas Smetana <tsmetana@redhat.com> 20070628-1.1
- rebuild

* Thu Jul 12 2007 Tomas Smetana <tsmetana@redhat.com> 20070628-1
- new upstream version
- fix unaligned access messages (Related: #219420)

* Tue May 22 2007 Tomas Smetana <tsmetana@redhat.com> 20070328-2
- fix wrong exit status of spawned process after SIGSTOP
- fix building of debuginfo package, add %%{?dist} to release
- fix handling of SIGTTOU in non-interactive shell
- remove useless builtins

* Thu Apr 19 2007 Tomas Smetana <tsmetana@redhat.com> 20070328-1
- new upstream source
- fix login shell invocation (#182397)
- fix memory leak

* Wed Feb 21 2007 Karsten Hopp <karsten@redhat.com> 20070111-1
- new upstream version
- fix invalid write in uname function

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 20060214-1.1
- rebuild

* Thu Jun 01 2006 Karsten Hopp <karsten@redhat.de> 20060214-1
- new upstream source

* Mon Feb 27 2006 Karsten Hopp <karsten@redhat.de> 20060124-3
- PreReq grep, coreutils (#182835)

* Tue Feb 14 2006 Karsten Hopp <karsten@redhat.de> 20060124-2
- make it build in chroots (#180561)

* Mon Feb 13 2006 Karsten Hopp <karsten@redhat.de> 20060124-1
- version 20060124

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 20050202-5.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Karsten Hopp <karsten@redhat.de> 20050202-5
- rebuild

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 20050202-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Feb 02 2006 Karsten Hopp <karsten@redhat.de> 20050202-4
- fix uname -i output
- fix loop (*-path.patch)
- conflict pdksh instead of obsoleting it

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com> 20050202-3.1
- rebuilt for new gcj

* Tue May 10 2005 Karsten Hopp <karsten@redhat.de> 20050202-3
- enable debuginfo

* Tue Mar 15 2005 Karsten Hopp <karsten@redhat.de> 20050202-2
- add /usr/bin/ksh link for compatibility with pdksh scripts (#151134)

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 20050202-1 
- update and rebuild with gcc-4

* Tue Mar 01 2005 Karsten Hopp <karsten@redhat.de> 20041225-2 
- fix gcc4 build 

* Fri Jan 21 2005 Karsten Hopp <karsten@redhat.de> 20041225-1
- rebuild with new ksh tarball (license change)

* Tue Nov 02 2004 Karsten Hopp <karsten@redhat.de> 20040229-11
- disable ia64 for now

* Fri Oct 15 2004 Karsten Hopp <karsten@redhat.de> 20040229-9 
- rebuild

* Thu Sep 02 2004 Nalin Dahyabhai <nalin@redhat.com> 20040229-8
- remove '&' from summary

* Thu Sep 02 2004 Bill Nottingham <notting@redhat.com> 20040229-7
- obsolete pdksh (#131303)

* Mon Aug 02 2004 Karsten Hopp <karsten@redhat.de> 20040229-6
- obsolete ksh93, provide ksh93

* Mon Jul 05 2004 Karsten Hopp <karsten@redhat.de> 20040229-3 
- add /bin/ksh to /etc/shells

* Wed Jun 16 2004 Karsten Hopp <karsten@redhat.de> 20040229-2 
- add ppc64 patch to avoid ppc64 dot symbol problem

* Fri May 28 2004 Karsten Hopp <karsten@redhat.de> 20040229-1 
- initial version

