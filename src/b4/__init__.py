import email.parser
emlpolicy = email.policy.EmailPolicy(utf8=True, cte_type='8bit', max_line_length=None,
                                     message_factory=email.message.EmailMessage)
__VERSION__ = '0.15-dev'
    # linktrailermask = Message-ID: <%s>
    # If this is not set, we'll use what we find in
        logger.debug('Analyzing trailer_map (%s entries)', len(self.trailer_map))
            logger.debug('  matching patch_id %s from: %s', lmsg.git_patch_id, lmsg.full_subject)
                    logger.debug('  matched: %s', fmsg.msgid)
                        if fltr in lmsg.trailers:
                            logger.debug('  trailer already exists')
                            continue
                        if fltr in lmsg.followup_trailers:
                            logger.debug('  identical trailer received for this series')
                            continue
                        logger.debug('  carrying over the trailer to this series (may be duplicate)')
                        logger.debug('  %s', lmsg.full_subject)
                        logger.debug('    + %s', fltr.as_string())
                        logger.debug('      via: %s', fltr.lmsg.msgid)
                        lmsg.followup_trailers.append(fltr)
    def add_message(self, msg: email.message.EmailMessage) -> None:
                     allowbadchars: bool = False, showchecks: bool = False) -> List[email.message.EmailMessage]:
                 msg: Optional[email.message.EmailMessage] = None):
    msg: email.message.EmailMessage
    references: List[str]
            self.references = [self.in_reply_to]
        else:
            self.references = list()
            for rbunch in self.msg.get_all('references', list()):
                for rchunk in LoreMessage.clean_header(rbunch).split():
                    rmsgid = rchunk.strip('<>')
                    if rmsgid not in self.references:
                        self.references.append(rmsgid)
            self.fromname = ''
            self.fromemail = ''
        if trailers and self.references and not self.has_diff and not self.reply:
            logger.debug('Examining: %s', ltr.as_string())
                logger.debug('  trailer email match with %s', self.fromemail)
                logger.debug('  trailer exact name match with %s', self.fromname)
                if nmatch:
                    logger.debug('  trailer fuzzy name match with %s', self.fromname)

            logger.debug('  trailer did not match: %s: %s', ltr.name, ltr.value)
    def run_local_check(cmdargs: List[str], ident: str, msg: email.message.EmailMessage,
        report = list()

        for line in out_lines:
            flag = 'fail' if 'ERROR:' in line else 'warning'
            # Remove '-:' from the start of the line, because it's never useful
            if line.startswith('-:'):
                line = line[2:]
            report.append((flag, f'{mycmd}: {line}'))

        err = err.strip()
        err_lines = err.decode(errors='replace').split('\n') if err else list()
        for line in err_lines:
            if line.startswith('-:'):
                line = line[2:]
            report.append(('fail', f'{mycmd}: {line}'))

        if (not out_lines) and (not err_lines):
            if ecode:
                report.append(('fail', f'{mycmd}: Exited with error code {ecode}'))
            else:
                report.append(('success', f'{mycmd}: passed all checks'))
    def get_payload(msg: email.message.EmailMessage, use_patch: bool = True) -> Tuple[str, str]:
    def get_msg_as_bytes(msg: email.message.EmailMessage, nl: str = '\n',
    def get_clean_msgid(msg: email.message.EmailMessage, header: str = 'Message-Id') -> Optional[str]:
    def get_preferred_duplicate(msg1: email.message.EmailMessage,
                                msg2: email.message.EmailMessage) -> email.message.EmailMessage:
        ignores = {'phone', 'email', 'prerequisite-message-id'}
        if '\n' in line:
            key, value = line.split('\n', 1)
        else:
            key, value = line, 'true'
def _val_to_path(topdir: str, val: str) -> str:
    if val.startswith('./'):
        # replace it with full topdir path
        return os.path.abspath(os.path.join(topdir, val))
    else:
        return val


    multivals = ['keyringsrc', 'am-perpatch-check-cmd', 'prep-perpatch-check-cmd']
            wtconfig = get_config_from_git(r'b4\..*', multivals=multivals, source=wtcfg)
                if key in multivals:
                    val = [_val_to_path(topdir, x) for x in val]
                else:
                    val = _val_to_path(topdir, val)
    config = get_config_from_git(r'b4\..*', defaults=defcfg, multivals=multivals)
        message = email.parser.BytesParser(policy=emlpolicy, _class=email.message.EmailMessage).parsebytes(
def get_strict_thread(msgs: Union[List[email.message.EmailMessage], mailbox.Mailbox, mailbox.Maildir],
                      msgid: str, noparent: bool = False) -> Optional[List[email.message.EmailMessage]]:
def mailsplit_bytes(bmbox: bytes, outdir: str, pipesep: Optional[str] = None) -> List[email.message.EmailMessage]:
                msgs.append(email.parser.BytesParser(policy=emlpolicy,
                                                     _class=email.message.EmailMessage).parsebytes(chunk))
            msgs.append(email.parser.BytesParser(policy=emlpolicy, _class=email.message.EmailMessage).parse(fh))
                          full_threads: bool = True) -> Optional[List[email.message.EmailMessage]]:
                msgs.append(email.parser.BytesParser(policy=emlpolicy, _class=email.message.EmailMessage).parse(fh))
def split_and_dedupe_pi_results(t_mbox: bytes, cachedir: Optional[str] = None) -> List[email.message.EmailMessage]:
def get_series_by_msgid(msgid: str, nocache: bool = False) -> Optional['LoreMailbox']:
    lmbx = LoreMailbox()
    t_msgs = get_pi_thread_by_msgid(msgid, nocache=nocache)
    if t_msgs:
        for t_msg in t_msgs:
            lmbx.add_message(t_msg)

    return lmbx


def get_pi_thread_by_url(t_mbx_url: str, nocache: bool = False) -> Optional[List[email.message.EmailMessage]]:
                msgs.append(email.parser.BytesParser(policy=emlpolicy, _class=email.message.EmailMessage).parse(fh))
                           with_thread: bool = True) -> Optional[List[email.message.EmailMessage]]:
                         limit_committer: Optional[str] = None) -> List[Tuple[str, email.message.EmailMessage]]:
        ecode, out = git_run_command(
            gitdir,
            [
                'show',
                '--format=email',
                '--full-index',
                '--binary',
                '--patch-with-stat',
                '--encoding=utf-8',
                '--notes',
                '-B',
                '-M',
                '-C',
                commit,
            ],
            decode=False,
        )
        msg = email.parser.BytesParser(policy=emlpolicy, _class=email.message.EmailMessage).parsebytes(out)
def save_git_am_mbox(msgs: List[email.message.EmailMessage], dest: BinaryIO) -> None:
def save_mboxrd_mbox(msgs: List[email.message.EmailMessage], dest: BinaryIO, mangle_from: bool = False) -> None:
    _basecfg = get_config_from_git(r'sendemail\.[^.]+$', multivals=['smtpserveroption'])
    identity = config.get('sendemail-identity') or _basecfg.get('identity')
        sconfig = get_config_from_git(rf'sendemail\.{identity}\..*', multivals=['smtpserveroption'], defaults=_basecfg)
        server_option = sconfig.get('smtpserveroption')
        if server_option:
            smtp += server_option
def send_mail(smtp: Union[smtplib.SMTP, smtplib.SMTP_SSL, None], msgs: Sequence[email.message.EmailMessage],
                    for msg in in_mbx:  # type: email.message.EmailMessage
def map_codereview_trailers(qmsgs: List[email.message.EmailMessage],
    seen_msgids = set()
    if ignore_msgids is not None:
        seen_msgids.update(ignore_msgids)
    covers = dict()
            logger.debug('  looking at parent ref: %s', refmid)
                logger.debug('  found in qmid_map: %s', refmid)
                logger.debug('  subj: %s', _qmsg.full_subject)
                # Is it the cover letter?
                if (_qmsg.counter == 0 and (not _qmsg.counters_inferred or _qmsg.has_diffstat)
                        and _qmsg.msgid in ref_map):
                    logger.debug('  stopping: found the cover letter for %s', qlmsg.full_subject)
                    if _qmsg.msgid not in covers:
                        covers[_qmsg.msgid] = set()
                    covers[_qmsg.msgid].add(qlmsg.msgid)
                    break
                elif _qmsg.has_diff:
                        logger.debug('  pqpid: %s', pqpid)
                            logger.debug('  matched patch-id %s to %s', pqpid, qlmsg.full_subject)
    if not covers:
        return patchid_map

    # find all patches directly below these covers
    for cmsgid, fwmsgids in covers.items():
        logger.debug('Looking at cover: %s', cmsgid)
        for qmid, qlmsg in qmid_map.items():
            if qlmsg.in_reply_to == cmsgid and qlmsg.git_patch_id:
                pqpid = qlmsg.git_patch_id
                for fwmsgid in fwmsgids:
                    logger.debug('Adding cover follow-up %s to patch-id %s', fwmsgid, pqpid)
                    if pqpid not in patchid_map:
                        patchid_map[pqpid] = list()
                    patchid_map[pqpid].append(qmid_map[fwmsgid])
