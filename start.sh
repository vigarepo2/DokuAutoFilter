if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://vigarepo2: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@github.com/vigarepo2/DokuAutoFilter /Eva
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Eva
fi
cd /Eva
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
