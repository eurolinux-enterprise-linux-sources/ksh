%define       releasedate   2012-08-01

Name:         ksh
Summary:      The Original ATT Korn Shell
URL:          http://www.kornshell.com/
Group:        System Environment/Shells
#zlib is used for INIT.2010-02-02.tgz/src/cmd/INIT/ratz.c - used only for build tool
#CPL everywhere else (for KSH itself)
License:      EPL
Version:      20120801
Release:      34%{?dist}
Source0:      http://www.research.att.com/~gsf/download/tgz/ast-ksh.%{releasedate}.tgz
Source1:      http://www.research.att.com/~gsf/download/tgz/INIT.%{releasedate}.tgz
Source2:      kshcomp.conf
Source3:      kshrc.rhs
Source4:      dotkshrc

# expected results of test suite
%global testresults  %{_sourcedir}/expectedresults.log

# don't use not wanted/needed builtins - Fedora/RHEL specific
Patch1:       ksh-20070328-builtins.patch

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

# for ksh <= 2013-04-19, rhbz#913110
Patch27:      ksh-20120801-macro.patch

# not completely upstream yet, rhbz#858263
Patch29:      ksh-20130628-longer.patch

# fix regression test suite to be usable during packagebuild - Fedora/RHEL specific
Patch99:      ksh-20100826-fixregr.patch

# for ksh <= 2013-07-19, rhbz#982142
Patch30: ksh-20120801-mlikfiks.patch

# not yet upstream, related to 2012-08-01 rebase
Patch31: ksh-20120801-covsfix.patch

# rhbz#1007816
Patch32: ksh-20100621-manfix3.patch

# rhbz#1016611
Patch33: ksh-20120801-nomulti.patch

# for ksh <= 2014-01-14, rhbz#
Patch34: ksh-20120801-mtty.patch

# from upstream, rbzh#1048272
Patch35: ksh-20120801-fd2lost.patch

# sent upstream 2014-01, rhbz#1047507
Patch36: ksh-20120801-argvfix.patch

# for ksh <= 2014-01-14, rhbz#1048995
Patch37: ksh-20120801-memlik3.patch

# for ksh <= 2013-04-09, rhbz#960371
Patch38: ksh-20120801-lexfix.patch

# not yet upstream, for ksh <= 2014-02-26, rhbz#1070328
Patch39: ksh-20120801-filecomsubst.patch

# for ksh <= 2014-06-25, rhbz#825520,rhbz#1084406
Patch40: ksh-20120801-crash.patch

# for ksh < 2013-03-19, rhbz#1085385
Patch41: ksh-20120801-sufix.patch

# sent upstream, rhbz#1099935
Patch42: ksh-20140301-fikspand.patch

# for ksh < 2014-04-15, rhbz#1070871
Patch43: ksh-20120801-roundit.patch

# for ksh < 2014-04-15, rhbz#1111120
Patch44: ksh-20120801-heresub.patch

# not included upstream yet, rhbz#1077090
Patch45: ksh-20140415-hokaido.patch

# for ksh < 2012-10-04, rhbz#1121960
Patch46: ksh-20120801-tpstl.patch

# sent upstream, rhbz#1100215
Patch47: ksh-20120801-manfix4.patch

# not upstream yet, rhbz#1100215
Patch48: ksh-20120801-fununset.patch

# for ksh < 2014-06-25, rhbz#1109893
Patch49: ksh-20120801-cdfix3.patch

# sent upstream, rhbz#1116506
Patch50: ksh-20120801-locking.patch

# for ksh <= 2013-06-13, rhbz#1133585
Patch51: ksh-20130613-cdfix4.patch

Patch52: ksh-20120801-retfix.patch

# sent upstream, for ksh <= 2014-09-30
Patch53: ksh-20120801-cdfork.patch

# not upstream yet, for ksh <= 2015-04-03, rhbz#1200534
Patch54: ksh-20140801-arraylen.patch

# sent upstream, for ksh <= 2014-09-29, rhbz#1212993
Patch55: ksh-20140801-diskfull.patch

# not upstream yet, rhbz#1192026
Patch56: ksh-20120801-xufix.patch

# sent upstream, for ksh <= 2014-12-18, rhbz#1192119
Patch58: ksh-20120801-alarmifs.patch

# not yet upstream, rhbz#1202439
Patch59: ksh-20140929-safefd.patch

# workaround, for ksh < 2013-05-24, rhbz#1211540
Patch60: ksh-20120801-trapcom.patch

# not yet upstream, rhbz#1217237
Patch64: ksh-20120801-nohupfork.patch

# from upstream, for ksh <= 20130409, rhbz#1241014
Patch65: ksh-20120801-parserfix.patch

# not upstream yet, rhbz#1211538
Patch66: ksh-20120801-oldenvinit.patch

# from upsteam, for ksh < 2012-10-04, rhbz#1193557
Patch67: ksh-20120801-emptyarrayinit.patch

# not upstream yet, rhbz#1371630
Patch68: ksh-20120801-typeset.patch

# not upstream yet, rhbz#1321443
Patch69: ksh-20120801-dotdoublefree.patch

# not upstream yet, rhbz#1405784
Patch70: ksh-20120801-subshell-leak.patch

# rhbz#1189297
Patch71: ksh-20120801-assoc-unset-leak.patch

# rhbz#1222025
Patch72: ksh-20120801-unset-param.patch

# rhbz#1269088
Patch73: ksh-20120801-badgcc.patch

# rhbz#1299484
Patch74: ksh-20120801-mb-after-argvar.patch

BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Conflicts:    pdksh
Requires: coreutils, diffutils, chkconfig
# regression test suite uses 'ps' from procps
BuildRequires: procps, bison
Requires(post): grep, coreutils, chkconfig, systemd-units
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
%patch6 -p1 -b .manfix
%patch17 -p1 -b .pathvar
%patch99 -p1 -b .fixregr
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
%patch29 -p1 -b .longer
%patch30 -p1 -b .mlikfiks
%patch31 -p1 -b .covsfix
%patch32 -p1 -b .manfix3
%patch33 -p1 -b .nomulti
%patch34 -p1 -b .mtty
%patch35 -p1 -b .fd2lost
%patch36 -p1 -b .argvfix
%patch37 -p1 -b .memlik3
%patch38 -p1 -b .lexfix
%patch39 -p1 -b .filecomsubst
%patch40 -p1 -b .crash
%patch41 -p1 -b .sufix
%patch42 -p1 -b .fikspand
%patch43 -p1 -b .roundit
%patch44 -p1 -b .heresub
%patch45 -p1 -b .hokaido
%patch46 -p1 -b .tpstl
%patch47 -p1 -b .manfix4
%patch48 -p1 -b .fununset
%patch49 -p1 -b .cdfix3
%patch50 -p1 -b .locking
%patch51 -p1 -b .cdfix4
%patch52 -p1 -b .retfix
%patch53 -p1 -b .cdfork
%patch54 -p1 -b .arraylen
%patch55 -p1 -b .diskfull
%patch56 -p1 -b .xufix
%patch58 -p1 -b .alarmifs
%patch59 -p1 -b .safefd
%patch60 -p1 -b .trapcom
%patch64 -p1 -b .nohupfork
%patch65 -p1 -b .parserfix
%patch66 -p1 -b .oldenvinit
%patch67 -p1 -b .emptyarrayinit
%patch68 -p1 -b .typeset_a
%patch69 -p1 -b .dotdoublefree
%patch70 -p1 -b .subshell-leak
%patch71 -p1 -b .assoc-unset-leak
%patch72 -p1 -b .unset-param
%patch73 -p1 -b .badgcc
%patch74 -p1 -b .mb-after-argvar

#/dev/fd test does not work because of mock
sed -i 's|ls /dev/fd|ls /proc/self/fd|' src/cmd/ksh93/features/options

# sh/main.c was not using CCFLAGS
sed -i '/-c sh\/main.c/s|${mam_cc_FLAGS} |${mam_cc_FLAGS} ${CCFLAGS} |p' src/cmd/ksh93/Mamfile

%build
XTRAFLAGS=""
for f in -Wno-unknown-pragmas -Wno-missing-braces -Wno-unused-result -Wno-return-type -Wno-int-to-pointer-cast -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable -Wno-cpp
do
  gcc $f -E - </dev/null >/dev/null 2>&1 && XTRAFLAGS="$XTRAFLAGS $f"
done
./bin/package
./bin/package make mamake ||:
./bin/package make mamake ||:
export CCFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing $XTRAFLAGS -DSHOPT_AUDIT"
export CC=gcc
./bin/package make -S


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{/bin,%{_bindir},%{_mandir}/man1}
install -c -m 755 arch/*/bin/ksh $RPM_BUILD_ROOT/bin/ksh93
install -c -m 755 arch/*/bin/shcomp $RPM_BUILD_ROOT%{_bindir}/shcomp
install -c -m 644 arch/*/man/man1/sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ksh93.1
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.kshrc
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/kshrc
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/binfmt.d/kshcomp.conf

ln -s /bin/ksh93 $RPM_BUILD_ROOT/bin/rksh

#fool rpmbuild about %ghost files
touch $RPM_BUILD_ROOT/bin/ksh
touch $RPM_BUILD_ROOT%{_mandir}/man1/ksh.1.gz

%check
[ -f ./skipcheck -o -f ./../skipcheck ] && exit 0 ||:
%if 0%{?rhel} > 6
%ifarch s390
exit 0
%endif
%endif

export SHELL=$(ls $(pwd)/arch/*/bin/ksh)
cd src/cmd/ksh93/tests/
ulimit -c unlimited
if [ ! -e /dev/fd ]
then
  echo "ERROR: /dev/fd does not exist, regression tests skipped"
  exit 0
fi
$SHELL ./shtests 2>&1 | tee testresults.log
ls core.* 2>/dev/null ||:
exit 0

%post
for s in /bin/ksh /bin/rksh
do
  if [ ! -f /etc/shells ]; then
        echo "$s" > /etc/shells
  else
        if ! grep -q '^'"$s"'$' /etc/shells ; then
                echo "$s" >> /etc/shells
        fi
  fi
done

/bin/systemctl try-restart systemd-binfmt.service >/dev/null 2>&1 || :
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
for s in /bin/ksh /bin/rksh
do
  if [ ! -f $s ]; then
	sed -i '\|^'"$s"'$|d' /etc/shells
  fi
done

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
%doc src/cmd/ksh93/COMPATIBILITY src/cmd/ksh93/RELEASE src/cmd/ksh93/TYPES 
# LICENSE file is missing, temporarily?
/bin/ksh93
/bin/rksh
%ghost /bin/ksh
/usr/bin/shcomp
%{_mandir}/man1/ksh93.1.gz
%ghost %{_mandir}/man1/ksh.1.gz
%config(noreplace) %{_sysconfdir}/skel/.kshrc
%config(noreplace) %{_sysconfdir}/kshrc
%config(noreplace) %{_sysconfdir}/binfmt.d/kshcomp.conf

%clean
    rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-34
- Multibyte character string after $1-9 was not expanded correctly
  Resolves: #1299484

* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-33
- Prevent null-test optimization in strdup
  Resolves: #1269088

* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-32
- Treat unset parameters as error
  Resolves: #1222025

* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-31
- Fix a memory leak on unset of associative array
  Resolves: #1189297

* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-30
- Fix a memory leak in subshell when PATH is set
  Resolves: #1405784

* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-29
- Fix a crash during clean up after sourcing multiple files
  Resolves: #1321443

* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-28
- Fix a bug in memory allocation while listing indexed arrays with typeset
  Resolves: #1371630

* Fri Feb 10 2017 Siteshwar Vashisht <svashisht@redhat.com> - 20120801-27
- bump release
  Resolves: #1391931

* Tue Apr 26 2016 Michal Hlavinka <mhlavink@redhat.com> - 20120801-26
- closing a file descriptor in a command substitution caused loss of the output (#1202439)
- fix: in a login shell "( cmd & )" does nothing (#1217237)
- exporting fixed with variable corrupted its data (#1192026)
- fix segfault when handling a trap (#1211540)
- combining alarm and IFS caused segfault (#1192119)
- declaration of a two dimemsional associatve array could add an extra 0 element (#1193557)
- do not inherit invalid variables during shell initializaton (#1211538)
- case in a for loop inside a subshell caused syntax error (#1241014)

* Wed Sep 30 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-25
- ksh could hang when executed from removed directory (#1204639)

* Tue Jun 02 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-24
- ksh crashed when disk was full (#1212993)

* Tue Apr 07 2015 Michal Hlavinka <mhlavink@redhat.com> - 20120801-23
- using trap DEBUG could cause segmentation fault (#1209383)

* Mon Nov 24 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-22
- fix postun scriptlet (#1146161)

* Tue Sep 30 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-21
- include symlink for restricted shell (#1146161)
- ksh hangs when command substitution containing pipe fills out the pipe buffer (#1138751)
- current directory could differ from PWD (#1135573)
- cd builtin could break IO redirection (#1133585)
- return code from a function could be wrong (#1116507)

* Tue Jul 22 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-20
- fix segfault in job list code (#1084406)
- do not resend signal on termination (#1085385)
- fix brace expansion on/off (#1099935)
- fix incorrect rounding of numsers 0.5 < |x| <1.0 in printf (#1070871)
- fix parser errors related to the end of the here-document marker (#1111120)
- ksh hangs when command substitution fills out the pipe buffer (#1077090)
- using typeset -l with a restricted variabled caused segmentation fault (#1121960)
- monitor mode was documented incorrectly (#1100215)
- do not crash when unsetting running function from another one (#1100215)
- should report an error when trying to cd into directory without execution bit (#1109893)
- job locking mechanism did not survive compiler optimization (#1116506)

* Wed Feb 26 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-19
- reading a file via command substitution did not work when any of stdin,
  stdout or stderr were closed (#1070328)

* Tue Feb 11 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-18
- fix lexical parser crash (#1062220)

* Thu Jan 30 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-17
- add missing patch and rebuild (#1048995)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 20120801-16
- Mass rebuild 2014-01-24

* Wed Jan 22 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-15
- fix argv rewrite (#1047507)
- fix memory leak (#1048995)
- standard error output could get misdirected (#1048272)

* Fri Jan 03 2014 Michal Hlavinka <mhlavink@redhat.com> - 20120801-14
- fix interactive mode hangs (#1034909)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20120801-13
- Mass rebuild 2013-12-27

* Tue Nov 26 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-12
- ksh sometimes wrote wrong byte sequence to terminal when vi editing 
  mode was used (#1026360)
- fix errors in man page (#1030867)

* Wed Oct 30 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-11
- ksh stops on read when monitor mode is enabled (#1023110)

* Wed Jun 12 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-10
- fix memory leak
- monitor mode in scripts wasn't working

* Fri May 24 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-9
- add alternatives switching with mksh

* Thu Mar 07 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-8
- fix another reproducer for tab completion

* Fri Feb 22 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-7
- do not segfault on kill % (#914669)

* Fri Feb 01 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-6
- cd file did not produce any error

* Fri Jan 25 2013 Michal Hlavinka <mhlavink@redhat.com> - 20120801-5
- ksh could not enter directories with path containing /.something (#889748)
- file name autocomplete prevented following numeric input (#889745)

* Wed Nov 21 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120801-4
- bind Home, End, Delete,... key correctly for emacs mode
- do not crash when executed from deleted directory

* Fri Sep 14 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120801-3
- fix typo in binfmt config file
- register binary format after package installation

* Thu Sep 13 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120801-2
- add support for direct execution of compiled scripts

* Wed Aug 08 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120801-1
- ksh updated to 20120801

* Tue Jul 31 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120727-1
- ksh updated to 2012-07-27

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120628-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120628-1
- ksh updated to 20120628

* Wed Jun 27 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120626-1
- ksh updated to 20120626

* Fri Jun 22 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120620-1
- ksh updated to 2012-06-20

* Wed Jun 13 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120612-1
- ksh updated to 20120612

* Mon Jun 04 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120531-1
- ksh updated to 2012-05-31

* Mon Mar 19 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120229-2
- do not hang after return code 12

* Wed Mar 14 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120229-1
- ksh updated to 2012-02-29

* Tue Mar 13 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120214-2
- fix tilda expansion in scripts

* Mon Feb 20 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120214-1
- ksh updated to 20120214

* Mon Feb 06 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120202-1
- ksh updated to 20120202

* Thu Jan 05 2012 Michal Hlavinka <mhlavink@redhat.com> - 20120101-1
- ksh updated to 2012-01-01

* Wed Dec 07 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-9
- do not crash when browsing through history containing comment (#733813)

* Wed Dec 07 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-8
- do not crash when two subseguent dots are used in variable or command name (#733544)

* Mon Dec 05 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-7
- fix: ksh can prematurely exit without crash or any error
- make spec work in epel

* Thu Nov 10 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-6
- add files to %%doc

* Thu Oct 06 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-5
- ksh sometimes returns wrong exit code when pid numbers are being recycled

* Tue Oct 04 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-4
- restore tty settings after timed out read (#572291)

* Fri Aug 12 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-3
- do not crash when killing last bg job when there is not any

* Wed Aug 03 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-2
- fix: IFS manipulation in a function can cause crash

* Fri Jul 01 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110630-1
- ksh updated to 2011-06-30

* Wed Jun 08 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110505-2
- fix: resume of suspended process using pipes does not work (#708909)

* Mon May 09 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110505-1
- ksh updated to 2011-05-05

* Fri Apr 29 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110428-1
- ksh updated to 2011-04-28

* Mon Apr 18 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110415-1
- ksh updated to 2011-04-15

* Tue Mar 29 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110208-3
- fix array definition being treated as fixed array
- fix suspend crashing ksh

* Mon Mar 07 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110208-2
- fix ( ) compound list altering environment

* Wed Feb 09 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110208-1
- ksh updated to 2011-02-08

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110202-1
- ksh updated to 2011-02-02

* Wed Feb 02 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110131-1
- ksh updated to 2011-01-31

* Fri Jan 28 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110127-1
- ksh updated to 2011-01-27

* Thu Jan 20 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110118-1
- ksh updated to 2011-01-18

* Mon Jan 17 2011 Michal Hlavinka <mhlavink@redhat.com> - 20110104-1
- ksh updated to 2011-01-04

* Thu Dec 23 2010 Michal Hlavinka <mhlavink@redhat.com> - 20101212-2.20101122
- found ugly regression, reverting to 2010-11-22 (with io race patch) for now

* Thu Dec 16 2010 Michal Hlavinka <mhlavink@redhat.com> - 20101212-1
- ksh updated to 2010-12-12

* Mon Dec 06 2010 Michal Hlavinka <mhlavink@redhat.com> - 20101201-2
- fix file io race condition when file was created, but still does not exist

* Fri Dec 03 2010 Michal Hlavinka <mhlavink@redhat.com> - 20101201-1
- ksh updated to 2010-12-01

* Tue Nov 23 2010 Michal Hlavinka <mhlavink@redhat.com> - 20101122-1
- ksh updated to 2010-11-22

* Mon Nov 01 2010 Michal Hlavinka <mhlavink@redhat.com> - 20101026-1
- ksh updated to 2010-10-26

* Tue Oct 12 2010 Michal Hlavinka <mhlavink@redhat.com> - 20101010-1
- ksh updated to 2010-10-10

* Fri Oct 08 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100924-2
- disable only known to be broken builtins, let other enabled
- skip regression tests if /dev/fd is missing

* Tue Sep 28 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100924-1
- ksh updated to 2010-09-24

* Mon Aug 30 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100826-1
- ksh updated to 2010-08-26
- make regression test suite usable during package build

* Fri Aug 13 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100811-1
- ksh updated to 2010-08-11

* Thu Jul 08 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100701-1
- updated to 2010-07-01

* Fri Jun 25 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100621-1
- updated to 2010-06-21

* Tue Jun 15 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100527-2
- add shcomp for shell compiling

* Thu Jun 10 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100527-1
- updated to 2010-05-27

* Mon May 31 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100309-6
- add pathmunge to /etc/kshrc

* Wed May 05 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100309-5
- fix rare cd builtin crash (#578582)

* Wed May 05 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100309-4
- fix infinite loop when whence builtin is used with -q option (#587127)
- fix stdin for double command substitution (#584007)

* Mon Mar 29 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100309-3
- fix typo in last patch

* Fri Mar 26 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100309-2
- restore tty settings after timed out read for utf-8 locale

* Wed Mar 10 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100309-1
- updated to 2010-03-09
- fix mock building - detection of /dev/fd/X

* Mon Jan 04 2010 Michal Hlavinka <mhlavink@redhat.com> - 20100202-1
- updated to 2010-02-02

* Mon Jan 04 2010 Michal Hlavinka <mhlavink@redhat.com> - 20091224-1
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

