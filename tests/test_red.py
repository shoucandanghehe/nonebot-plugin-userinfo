from nonebot.adapters.red import Bot, Message
from nonebot.adapters.red.api.model import (
    ChatType,
    Element,
    MsgType,
    RoleInfo,
    TextElement,
)
from nonebot.adapters.red.config import BotInfo
from nonebot.adapters.red.event import GroupMessageEvent, PrivateMessageEvent
from nonebug import App


def text_element(text: str) -> Element:
    return Element(
        elementType=1,
        elementId="1111",
        extBufForUI="0x",
        picElement=None,
        textElement=TextElement(
            content=text,
            atType=0,
            atUid="0",
            atTinyId="0",
            atNtUid="",
            atNtUin=None,
            subElementType=0,
            atChannelId="0",
            atRoleId="0",
            atRoleColor="0",
            atRoleName="",
            needNotify="0",
        ),
        arkElement=None,
        avRecordElement=None,
        calendarElement=None,
        faceElement=None,
        fileElement=None,
        giphyElement=None,
        grayTipElement=None,
        inlineKeyboardElement=None,
        liveGiftElement=None,
        markdownElement=None,
        marketFaceElement=None,
        multiForwardMsgElement=None,
        pttElement=None,
        replyElement=None,
        structLongMsgElement=None,
        textGiftElement=None,
        videoElement=None,
        walletElement=None,
        yoloGameResultElement=None,
    )


async def test_group_message_event(app: App):
    from nonebot_plugin_userinfo import UserInfo
    from nonebot_plugin_userinfo.image_source import QQAvatar
    from tests.plugins.echo import user_info_cmd

    event = GroupMessageEvent(
        msgId="7272944513098472702",
        msgRandom="1526531828",
        msgSeq="831",
        cntSeq="0",
        chatType=ChatType.GROUP,
        msgType=MsgType.normal,
        subMsgType=1,
        sendType=0,
        senderUid="4321",
        senderUin="1234",
        peerUid="1111",
        peerUin="1111",
        channelId="",
        guildId="",
        guildCode="0",
        fromUid="0",
        fromAppid="0",
        msgTime="1693364354",
        msgMeta="0x",
        sendStatus=2,
        sendMemberName="",
        sendNickName="uy/sun",
        guildName="",
        channelName="",
        elements=[text_element("/user_info")],
        message=Message("/user_info"),
        original_message=Message("/user_info"),
        records=[],
        emojiLikesList=[],
        commentCnt="0",
        directMsgFlag=0,
        directMsgMembers=[],
        peerName="uy/sun",
        editable=False,
        avatarMeta="",
        avatarPendant="",
        feedId="",
        roleId="0",
        timeStamp="0",
        isImportMsg=False,
        atType=0,
        roleType=None,
        fromChannelRoleInfo=RoleInfo(roleId="0", name="", color=0),
        fromGuildRoleInfo=RoleInfo(roleId="0", name="", color=0),
        levelRoleInfo=RoleInfo(roleId="0", name="", color=0),
        recallTime="0",
        isOnlineMsg=True,
        generalFlags="0x",
        clientSeq="0",
        nameType=0,
        avatarFlag=0,
    )
    user_info = UserInfo(
        user_id="1234",
        user_name="uy/sun",
        user_displayname="",
        user_remark=None,
        user_avatar=QQAvatar(qq=1234),
        user_gender="unknown",
    )
    async with app.test_matcher(user_info_cmd) as ctx:
        bot = ctx.create_bot(
            base=Bot,
            self_id="2233",
            info=BotInfo(port=1234, token="1234"),
        )
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, "", True, user_info=user_info)


async def test_bot_user_info(app: App):
    from nonebot_plugin_userinfo import UserInfo
    from nonebot_plugin_userinfo.image_source import QQAvatar
    from tests.plugins.echo import bot_user_info_cmd

    event = PrivateMessageEvent(
        msgId="7272944767457625851",
        msgRandom="196942265",
        msgSeq="103",
        cntSeq="0",
        chatType=ChatType.FRIEND,
        msgType=MsgType.normal,
        subMsgType=1,
        sendType=0,
        senderUid="4321",
        senderUin="1234",
        peerUid="4321",
        peerUin="1234",
        channelId="",
        guildId="",
        guildCode="0",
        fromUid="0",
        fromAppid="0",
        msgTime="1693364414",
        msgMeta="0x",
        sendStatus=2,
        sendMemberName="",
        sendNickName="",
        guildName="",
        channelName="",
        elements=[text_element("/bot_user_info")],
        message=Message("/user_info"),
        original_message=Message("/user_info"),
        records=[],
        emojiLikesList=[],
        commentCnt="0",
        directMsgFlag=0,
        directMsgMembers=[],
        peerName="",
        editable=False,
        avatarMeta="",
        avatarPendant="",
        feedId="",
        roleId="0",
        timeStamp="0",
        isImportMsg=False,
        atType=0,
        roleType=0,
        fromChannelRoleInfo=RoleInfo(roleId="0", name="", color=0),
        fromGuildRoleInfo=RoleInfo(roleId="0", name="", color=0),
        levelRoleInfo=RoleInfo(roleId="0", name="", color=0),
        recallTime="0",
        isOnlineMsg=True,
        generalFlags="0x",
        clientSeq="27516",
        nameType=0,
        avatarFlag=0,
    )
    user_info = UserInfo(
        user_id="2233",
        user_name="Bot",
        user_displayname=None,
        user_remark=None,
        user_avatar=QQAvatar(qq=2233),
        user_gender="male",
    )
    async with app.test_matcher(bot_user_info_cmd) as ctx:
        bot = ctx.create_bot(
            base=Bot,
            self_id="2233",
            info=BotInfo(port=1234, token="1234"),
        )
        ctx.receive_event(bot, event)
        ctx.should_call_api(
            "get_self_profile",
            {},
            {
                "uid": "u_5",
                "qid": "",
                "uin": "2233",
                "nick": "Bot",
                "remark": "",
                "longNick": "",
                "avatarUrl": "http://qh.qlogo.cn/g?b=qq&ek=xxx",
                "birthday_year": 0,
                "birthday_month": 0,
                "birthday_day": 0,
                "sex": 1,
                "topTime": "0",
                "isBlock": False,
                "isMsgDisturb": False,
                "isSpecialCareOpen": False,
                "isSpecialCareZone": False,
                "ringId": "0",
                "status": 10,
                "extStatus": 0,
                "categoryId": 0,
                "onlyChat": False,
                "qzoneNotWatch": False,
                "qzoneNotWatched": False,
                "vipFlag": False,
                "yearVipFlag": False,
                "svipFlag": False,
                "vipLevel": 1,
            },
        )
        ctx.should_call_send(event, "", True, user_info=user_info)
